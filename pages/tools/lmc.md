---
title: The Maude LTL Logical Model Checker
---

## Introduction

A concurrent system can be naturally specified as a rewrite theory (Σ,E,R).
Under simple conditions, narrowing with rules R modulo the equations E can be used to both represent the system's state space by means of terms with logical variables and for model checking verification of LTL properties.
Folding abstraction may approximate infinite logical reachable subsystem into a finite logical system.
The Maude LTL logical model checker (LMC) tool can verify LTL properties over such logical states from a pattern of (possibly infinite) initial states using the (folded) logical state space.

Using this method, one of four outcomes is possible: (i) a fixpoint (a finite state space) is reached and the formula is fully verified; (ii) no such fixpoint is reached and the formula is only verified up to a given bound; (iii) a real counterexample is found and reported; or (iv) a possibly spurious counterexample is found and reported.

## Documentation

The main feature and the usage of the Maude LMC tool are briefly described in this [tutorial](lmc/manual.pdf), where we illustrate the LMC tool using the examples below.

## References

The following paper explains approximation methods for logical model checking:

* *[Abstract Logical Model Checking of Infinite-State Systems Using Narrowing](http://dx.doi.org/10.4230/LIPIcs.RTA.2013.81)*, Kyungmin Bae, Santiago Escobar, José Meseguer, RTA'13, 2013

The narrowing-based symbolic model checking method is introduced in:

* *[Symbolic Model Checking of Infinite-State Systems Using Narrowing](http://dl.acm.org/citation.cfm?id=1779795)*, Santiago Escobar, José Meseguer, RTA'07, 2007

## Download

The Maude LMC model checker is available at the [maude-model-checker](https://github.com/kquine/maude-model-checker) repository on GitHub.

## Examples

The followings are logical model checking examples using our tool.

* [Lamport's Bakery protocol](lmc/examples/bakery.maude)
* [Readers-Writers problem](lmc/examples/rw-shared.maude)
* [Readers-Writers problem (simplified)](lmc/examples/rw.maude)
* [Dijkstra's mutual exclusion algorithm](lmc/examples/dijkstra-mutex.maude)
* [Burns's mutual exclusion algorithm](lmc/examples/burns-mutex.maude)
* [Token ring mutual exclusion](lmc/examples/token-mutex.maude)
* [Vending Machine example](lmc/examples/vending.maude)
* [Plotter example](lmc/examples/plotter-push.maude)

## Contact

[Kyungmin Bae](https://forever.postech.ac.kr/kmbae/)
