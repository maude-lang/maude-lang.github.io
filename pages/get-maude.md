---
title: Get Maude
---

Maude 3.5.1 runs on many Unix variants, including macOS and Linux. The
installation is straightforward, there is one single executable file
with no dependencies whatsoever. Nevertheless, some hints on how to use
it and how to install it in Windows platforms can be found below. 
The Maude system download consists of the Maude binaries, its
documentation, and some examples.

Maude 3.5.1 is currently available at [its GitHub site](https://github.com/SRI-CSL/Maude/releases/tag/Maude3.5.1)
for the following platforms:
* [Linux x86_64](https://github.com/maude-lang/Maude/releases/download/Maude3.5.1/Maude-3.5.1-linux-x86_64.zip)
* [macOS x64_64](https://github.com/maude-lang/Maude/releases/download/Maude3.5.1/Maude-3.5.1-macos-x86_64.zip)
* [macOS ARM](https://github.com/maude-lang/Maude/releases/download/Maude3.5.1/Maude-3.5.1-macos-arm64.zip)
* [Source code](https://github.com/maude-lang/Maude/archive/refs/tags/Maude3.5.1.tar.gz)

Some Linux distributions also offer Maude in
their official repositories
([Debian](https://packages.debian.org/stable/maude),
[Ubuntu](https://packages.ubuntu.com/maude),
[ArchLinux](https://archlinux.org/packages/extra/x86_64/maude/), etc.),
although their packages might not be up to date. Look [here](changes.md) for a list of changes since the previous release.

To install from one of the above binaries, simply extract the downloaded zip file. This generates the folder with the following files in it:

* `linear.maude`
* `machine-int.maude`
* `maude`
* `metaInterpreter.maude`
* `model-checker.maude`
* `prelude.maude`
* `process.maude`
* `smt.maude`
* `socket.maude`
* `term-order.maude`
* `time.maude`

You can now run Maude by starting the appropriate executable `maude` file. See the installation guidelines below if you need further help.

## Maude manual

The manual for Maude 3.5.1 and the code of the examples in it is available in the [documentation](documentation.md) section.

## Installation guidelines

In this section, we assume a Linux configuration. Please, substitute
your platform name for `linux` in what follows if you download for
another platform. In any case, please consider subscribing to the [Maude
users mailing list](lists.md), as this is also the
mechanism by which we will make announcements about the system.

As explained above, Maude has a single
executable that can be allocated anywhere in you machine. However, there
are several things you must take into account:

* Most Linux distributions allow the installation of Maude through
  their package management systems. It is not always updated though.
  We recommend to download the latest version directly from [Maude\'s
  official distribution site](https://github.com/SRI-CSL/Maude/releases/).

* The compressed file distributed in Maude\'s official site includes,
  in addition to the executable files (for Linux and macOS), several
  text files with Maude specifications. Maude tries to load one of
  them at start up, the `prelude.maude` file. The Maude interpreter
  checks for it in several directories, in the following order:
    1. the directories specified in the `MAUDE_LIB` environment variable,
    2. the directory containing the executable, and
    3. the current directory.

It may be the case that you know more than us on how to administer your
machine, but just some basic advise in case of need:

* In a Linux/macOS installation, you can unzip the distribution file
  anywhere in you disk. You can then add the folder in which it is
  located to your `PATH` environment variable, or create an alias or
  soft link in your `/usr/local/bin/` folder. You choose. If you prefer
  you can move to the folder or provide the entire path to execute it.

* And it is not only the `prelude.maude` file, the interpreter will
  follow this strategy when trying lo load any file. Therefore, it
  might be a good idea to include the path to the `prelude.maude` file
  in the MAUDE_LIB environment variable to be sure that it will always
  be found.

* If you are using a macOS machine, your system may still prevent it
  from being executed since you have downloaded it from an unknown
  source. You need to go to *System Preferences*, then *Security &
  Privacy (General)*, and grant permission.

Maude\'s manual includes information on how to run Maude and how to load
simple specifications (see [Maude Manual\'s Chapter
2](https://maude.lcc.uma.es/maude-manual/maude-manualch2.html#x13-22001)).

The Maude interpreter is all you need to run Maude programs. It is a
command line tool, with no graphical user interface. You can write your
specs directly in the terminal, but it is more convenient to use some
editor to create them and then load them in the interpreter. Maude
packages are available for more common text editors (Emacs, Visual
Studio Code, Atom, Sublime, \...), check on your favorite editor\'s
package management tool for it.

If you are a Windows user, our recommendation is to use
[WSL](https://docs.microsoft.com/en-us/windows/wsl). Follow the
instructions there to install it. Then you can install Maude as in
Linux/MacOS, and you can use Maude from the terminal or invoking it from
some tool. For instance, some users like to use Atom facilities for
invoking Maude directly from Atom. If you don\'t want to install WSL,
the FADoSS group distributes a Windows version of Maude. You can
download it from their site for [Maude\'s strategy
language](https://maude.ucm.es/strategies/maude+strat-windows.zip).

If you haven't been able to install it, please, contact us through the
[Maude help mailing list](mailto:maude-help@cs.illinois.edu).
