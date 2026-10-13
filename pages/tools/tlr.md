---
title: The Maude Linear Temporal Logic of Rewriting Model Checker
---

## Introduction

The Linear Temporal Logic of Rewriting (LTLR) is a state/event based extension of LTL with *spatial action patterns* which represent rewrite events. LTLR describes a property involving both events and state predicates, including *mixed* properties such as fairness. The Maude LTLR model checker is an explicit state model checker within the [Maude system](http://maude.cs.illinois.edu/).

Our Maude LTLR model checker can verify LTLR properties under *localized fairness* assumptions, which are parameterized fairness conditions over certain system entities.
A good example of parametric fairness is provided by object fairness assumptions such as “each object `o` infinitely often enabled to receive a message of the form `m(o,q)` will receive it infinitely often,” which is universally quantified over all the (possibly dynamically changing) objects `o` in the system.
Such universal quantification is succinctly captured by the notion of localized fairness; for example, fairness localized to the parameter `o` in object fairness conditions.

The Maude LTLR model checker is implemented at the C++ level by extending the existing Maude LTL model checker.
Unlike our [previous rewriting-based LTLR model checker](https://maude.cs.illinois.edu/tools/tlr/old) based on a theory and formula transformation, our new implementation do not cause any increase in the state space.

## Download

The Maude LTLR model checker is available at the [maude-model-checker](https://github.com/kquine/maude-model-checker) repository on GitHub.

## Examples

The followings are LTLR model checking examples using our tool. Some of them have localized fairness specification (see our [SCP paper](http://dx.doi.org/10.1016/j.scico.2014.02.006) for more details).

* [Evolving Dining Philosophers](tlr/examples/philo-dynamic.maude) (c.f., [Classical Dining Philosophers](tlr/examples/simple-dp.maude))
* [Blanced Sliding Window Protocol](tlr/examples/swp.maude)
* [Simple Client-Server model](tlr/examples/client-server.maude)
* [Dekker's Algorithm](tlr/examples/dekker.maude)
* [Bounded retransmission protocol](tlr/examples/brp-ltlr.maude) (see the [specification by LTL](tlr/examples/brp-ltl.maude) for the comparison.)
* [Unordered-channel](tlr/examples/unordered-channel.maude)
* [Position fairness](tlr/examples/context.maude)

## Reference

The Maude Fair LTLR Model checker is illustrated at:

* *[Model Checking Linear Temporal Logic of Rewriting Formulas under Localized Fairness](http://dx.doi.org/10.1016/j.scico.2014.02.006)*, Kyungmin Bae and José Meseguer, Science of Computer Programming, 2014 (To appear)
* *[Model Checking LTLR Formulas under Localized Fairness](http://dx.doi.org/10.1007/978-3-642-34005-5_6)*, Kyungmin Bae and José Meseguer, 9th International Workshop on Rewriting Logic and its Applications (WRLA), 2012

The parameterized fair model checking algorithm and localized fairness are presented in:

* *[State/Event-Based LTL Model Checking under Parametric Generalized Fairness](http://www.springerlink.com/content/7x6871u265524753/)*, Kyungmin Bae and José Meseguer, 23th International Conference on Computer Aided Verification (CAV), 2011
* *[Localized Fairness: A Rewriting Semantics](http://www.springerlink.com/content/h7xknutjhckjxmcv/)*, José Meseguer, 16th International Conference on Rewriting Techniques and Applications (RTA), 2005

The automata-theoretic foundation, design, and implementation of the Maude LTLR Model Checker is illustrated at:

* *[The Linear Temporal Logic of Rewriting Maude Model Checker](http://www.springerlink.com/content/3552hw4t52388h2v/)*, Kyungmin Bae and José Meseguer, 8th International Workshop on Rewriting Logic and its Applications (WRLA), 2010
* *[A Rewriting-Based Model Checker for the Linear Temporal Logic of Rewriting](http://sewiki.iai.uni-bonn.de/_media/rule08/rule08-bae.pdf?id=rule08%3Aprogram&cache=cache)*, Kyungmin Bae and José Meseguer, The 9th International Workshop on Rule-Based Programming, 2008

The following papers introduces the temporal logic of rewriting, the family of logics incorporating spatial action patterns.

* *[The Temporal Logic of Rewriting: A Gentle Introduction](http://www.springerlink.com/content/u1p55520u2352442)*, José Meseguer, LNCS 5065, 2008
* *[The Temporal Logic of Rewriting](https://www.ideals.illinois.edu/handle/2142/11293)*, José Meseguer, Technical Report UIUCDCS-R-2007-2815, CS Dept., University of Illinois at Urbana-Champaign, 2007

## Contact

[Kyungmin Bae](https://forever.postech.ac.kr/kmbae/)
