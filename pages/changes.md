---
title: Release notes
---

This page lists the main changes or release notes for each Maude release. They are also available in the [*Releases* section](https://github.com/maude-lang/Maude/releases) of the Maude repository.

## Maude 3.5.1

* New `LTL+` and `MODEL-CHECKER+` modules for easily obtaining witnesses of LTL properties
* Fixed several bugs related to module instantiation and `op to term` and `strat to expr` mappings
* Sort, class, and view naming restrictions are now checked and enforced
* Other bug fixes

## Maude 3.5

* Several changes related to the `vu-narrow` command:
    * `vfold` option,
    * `path` option,
    * a state may now subsume its ancestors,
    * allow term disjunctions at the object level,
    * `show most general states` command, and
    * `show frontier states` command
* Reading from the stdin stream now supports continuation lines
* Improvement of the initial equality operator
* Extra built-in operators on characters and strings
* Various optimizations
* Many bug fixes

## Maude 3.4

* Pseudo-random number generator objects
* Initial equality operator
* Meta-print to string operator and message pair
* LaTeX support
* `=>#` search type
* Various optimizations
* Many bug fixes

## Maude 3.3.1

* Some overparsing has been added to provide more informative hints on user input.
* Some bugs fixed.

## Maude 3.3

* Support for object-oriented features, including object-oriented modules and theories. Classes and messages can now be declared in object-oriented modules and theories, with multiple inheritance and their semantics specified using object-oriented statements that are automatically completed to simplify the specification of object-oriented systems. The handling of object-oriented features has been implemented as syntactic sugar, once entered object-oriented modules and theories are transformed into corresponding system modules and theories.
* The module system has been extended to support the new object-oriented features. Elements in object-oriented modules can be renamed when imported, and object-oriented parameterized modules can be instantiated using views from object-oriented theories. All other modules operations have been correspondingly extended.
* Modules can now be imported in a new `generated-by` mode.
* Some new commands and flags have been added.
* Constants can be declared as parameters in theories, and be parameterized in parameterized modules.
* Full Maude is no longer distributed as part of Maude. It is still available from the [Full Maude\'s GitHub site](https://github.com/maude-team/full-maude).
* Some over parsing has been added to better recover and to provide more informative hints on user input.
* Some bugs fixed.

## Maude 3.2.2

* Improvement on the `vu-narrow` command

## Maude 3.2

* Support for filtered variant unification in `vu-narrow` command,
* Several improvements in unification modulo several axioms,
* Several improvements of the external Maude I/O objects,
* A command flag for the depth of searching for A/AU unifiers, and
* Some bugs fixed.

## Maude 3.1

* Support for unification modulo associativity-identity,
* Support for the generation of irredundant unifiers,
* Support for the filtering of variant unifiers using variant subsumption,
* Support for the generation of variant matchers,
* An implementation of Unix processes as Maude external objects,
* Several improvements in the presentation of results,
* Several improvements in the handling of control-c,
* Some bugs fixed, and
* Some improvements in syntax error detection and recovering.

## Maude 2.6

* Order sorted ACU unification.
* Some additional overparsing to gracefully recover from typical syntactical errors.
* Several bugs fixed.

Changes for older releases can be found in the [*Releases* section](https://github.com/maude-lang/Maude/releases) of the Maude repository.
