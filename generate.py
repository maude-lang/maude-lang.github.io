#
# Maude web generator
#

# Possible improvements:
# - Include the update date based on the last modification in Git

import asyncio
from datetime import datetime
from pathlib import Path
import re
import shutil
import sys
import tomllib

from jinja2 import Environment, PackageLoader, select_autoescape
from latex2mathml.converter import convert as latex2mathml
from markdown_it import MarkdownIt
from mdit_py_plugins.anchors import anchors_plugin
from mdit_py_plugins.attrs import attrs_block_plugin, attrs_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.front_matter import front_matter_plugin
import yaml
# from pybtex.database import parse_file as parse_bibtex_file

# Source directory for the website pages in Markdown
SOURCE = Path('pages')
# Extension for HTML files
HTML_EXTENSION = '.html'
# Regex for citations in Pandoc format
CITE_REGEX = re.compile(r'\[@([A-Za-z0-9_-]+)\]')


def sync_to(origin: Path, destination: Path):
	"""Move all files from origin to destination"""

	for root, _, files in origin.walk():
		other_root = destination / root.relative_to(origin)

		if not other_root.exists():
			other_root.mkdir()

		for elem in files:
			# Original file and its copy in the destination directory
			original = root / elem
			other = other_root / elem

			if not other.exists() or original.stat().st_mtime > other.stat().st_mtime:
				shutil.copy(original, other)


def citation_rule(state, silent):
	"""Rule to parse citations"""

	# Look for [@name]
	if (m := CITE_REGEX.match(state.src[state.pos:])) is None:
		return False

	name = m.group(1)
	token = state.push('cite', '', 0)
	token.content = name

	state.pos += len(m.group(0))
	return True


def render_citation(self, tokens, idx, options, env):
	"""Render a citation"""

	name = tokens[idx].content
	return f'[<cite>{name}</cite>]'


def render_link(self, tokens, idx, options, env):
	"""Render a link"""

	token = tokens[idx]
	target = token.attrs['href']

	class_attr = ''

	# External link
	if target.startswith('http'):
		class_attr = ' class="external-link"'

	# Markdown pages
	elif target.endswith('.md'):
		# Make broken links visible
		if not (SOURCE / target).exists():
			class_attr = ' class="broken-link"'

		target = env['generator'].make_page_link(target[:-3])

	# Resource
	elif target.startswith(':') and '/' in target:
		prefix, name = target.split('/', maxsplit=1)
		target = env['generator'].make_resource_link(prefix[1:], name)

	return f'<a href="{target}"{class_attr}>'


def render_math_inline(self, tokens, idx, options, env):
	"""Render math"""

	content = tokens[idx].content
	return latex2mathml(content)


class SiteGenerator:
	"""Generator of the Maude website"""

	def __init__(self, args, config):
		# Save the configuration and arguments
		self.config = config
		self.output_path = args.o
		self.prefix = args.prefix
		self.current_prefix = args.prefix
		self.use_extension = args.ext

		# Generate templates for this
		self.env = Environment(
			loader=PackageLoader('generate'),
			autoescape=select_autoescape()
		)

		# Load the general template
		self.site_tmpl = self.env.get_template('site.htm')

		# Prepare the Markdown renderer
		self.md = (
		    MarkdownIt('commonmark', {'html': True})
		    .enable('table')
		    .use(dollarmath_plugin)
		    .use(anchors_plugin)
		    .use(attrs_plugin)
		    .use(attrs_block_plugin)
		    .use(front_matter_plugin)
		)

		self.md.inline.ruler.push('cite', citation_rule)
		self.md.add_render_rule('link_open', render_link)
		self.md.add_render_rule('math_inline', render_math_inline)
		self.md.add_render_rule('cite', render_citation)

		# Bibliography
		self.bibliography = {}

	def make_page_link(self, path):
		"""Make an internal page link"""

		# Make index page links point to the root 
		if not self.use_extension and path == 'index':
			return self.current_prefix

		return f'{self.current_prefix}{path}{HTML_EXTENSION if self.use_extension else ""}'
	
	def make_resource_link(self, ns, name):
		"""Make a link to a resource"""

		return self.config.get('release-path', 'missing').format(ns=ns, name=name)
	
	async def index_site(self, generated_files):
		"""Index the website for search"""

		from pagefind.index import PagefindIndex, IndexConfig

		index_config = IndexConfig(output_path=str(self.output_path / 'pagefind'))

		# Pagefind seems to add the prefix, so we do not do it again
		real_prefix, self.current_prefix = self.current_prefix, ''

		async with PagefindIndex(config=index_config) as index:
			# Index each generated file
			for file in generated_files:
				content = file.read_text()
				url = file.relative_to(self.output_path)

				await index.add_html_file(
					content=content,
					url=self.make_page_link(url.with_suffix('')),
					source_path=str(url),
				)

		self.current_prefix = real_prefix

	def generate(self):
		"""Generate the site"""

		# Copy static files
		sync_to(Path('static'), self.output_path)

		# Load bibliography
		# for source in self.config.get('bibliography', ()):
		# 	self.bibliography[source] = parse_bibtex_file(source)

		now = datetime.now()
		toc = self.config['toc']
		generated_files = []

		for page in SOURCE.rglob('*.md'):
			# Parse the input file
			page_tree = self.md.parse(page.read_text())

			# Page the page metadata
			metadata = {}

			if page_tree and page_tree[0].type == 'front_matter':
				metadata = yaml.safe_load(page_tree[0].content)

			# Look for the title header
			title = metadata.get('title', page.name.title())

			# Render content to HTML5
			html = self.md.renderer.render(page_tree, self.md.options, env={'generator': self})

			# Adjust prefix
			if self.prefix is None:
				self.current_prefix = f'{SOURCE.relative_to(page.parent, walk_up=True)}/' if page.parent != SOURCE else ''

			# Render the full page with Jinja
			source_path = page.relative_to(SOURCE)
			target_path = self.output_path / source_path.with_suffix(HTML_EXTENSION)
			target_path.parent.mkdir(exist_ok=True)

			self.site_tmpl.stream(
				current=str(source_path.with_suffix('')), # current page path
				content=html, # page content
				toc=toc,  # table of contents
				year=now.year,  # current year
				title=title,  # page title
				prefix=self.current_prefix,  # prefix of the site
				make_page_link=self.make_page_link,  # page link builder
			).dump(str(target_path))

			generated_files.append(target_path)

		# Generate the index
		asyncio.run(self.index_site(generated_files))


def main():
	import argparse

	parser = argparse.ArgumentParser(description='Maude website generator')
	parser.add_argument('-o', help='Output path for the generated site', type=Path, default=Path('output'))
	parser.add_argument('--prefix', '-p', help='Web server prefix')
	parser.add_argument('--no-ext', help='Omit extensions for internal links', action='store_false', dest='ext')

	args = parser.parse_args()

	# Create the output directory
	args.o.mkdir(exist_ok=True)

	# Load the site settings
	with open('site.toml', 'rb') as tomlf:
		config = tomllib.load(tomlf)

	SiteGenerator(args, config).generate()


if __name__ == '__main__':
	sys.exit(main())
