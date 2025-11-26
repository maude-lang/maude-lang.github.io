## Maude website source

This is the source code of the Maude website. Every page is a Markdown file in the `pages` directory, `static` includes the static files (images, stylesheets, etc.), and general settings are written in `site.toml`. The website is built by `generate.py` using the HTML template in `templates` and some external libraries.
```console
$ python generate.py
```
The Maude 1 website and some tool pages are downloaded as a compressed bundle from the releases of this repository and merged with the new generated page. Other static resources are also stored in the releases and linked from the Markdown pages with paths of the form `:tag/name`.
