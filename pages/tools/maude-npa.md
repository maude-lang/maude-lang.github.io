---
title: Maude-NPA
---

This webpage describes version 3.1.4 of the Maude-NRL Protocol Analyzer
(Maude-NPA) and gives instructions for its use.

Maude-NPA is an analysis tool for cryptographic protocols that takes
into account many of the algebraic properties of crypto systems that are
not included in other tools. These include cancellation of encryption
and decryption, Abelian groups (including exclusive-or), exponentiation,
and homomorphic encryption. Maude-NPA uses an approach similar to the
original NRL Protocol Analyzer; it is based on unification, and performs
backwards search from a final state to determine whether or not it is
reachable. Unlike the original NPA, it has a theoretical basis in
rewriting logic and narrowing, and offers support for a wider basis of
equational theories that includes commutative (C),
associative-commutative (AC), and associative-commutative-identity (ACU)
theories.

We provide below a detailed manual of installation and how to use
Maude-NPA, with several protocol examples. A description of Maude-NPA\'s
formal foundations in rewriting logic, together with a soundness proof,
is given in \[1\]. Descriptions of how Maude-NPA handles different
equational theories are given in \[2, 3, 5, 8, 9, 13, 15\]. API
Protocols are considered in \[16, 17\].

A forward semantics is presented in \[14\]. Several optimizations
included into Maude-NPA for improving the performance and reducing the
search space are introduced in \[4, 5, 12\]. A framework for protocol
analysis with asymmetric unification is given in \[10, 11\]. The
inclusion of disequality constraints is introduced in \[18\]. Sequential
protocol composition is introduced in \[7\]. And a process algebra is
introduced in \[19\].

A graphical interface for Maude-NPA was presented in \[6\] and is
publicly available at
[www.csl.sri.com/users/iam/NPA/index.html](http://www.csl.sri.com/users/iam/NPA/index.html).

## Maude Protocol Specification Language (Maude-PSL)

An experimental specification language for the Maude-NPA has been
developed by Andrew Cholewa in Spring 2015. It has the following
advantages:

1. Syntax based off of a conservative extension of the Alice and Bob
   notation that is both easier to read and write than the current
   input language.
2. More stringent error checking.
3. Significantly less code repetition.

A Github repository of the language can be found
[here](https://www.github.com/archolewa/Maude-PSL). In addition to the
source code, the repository also contains a collection of example
specifications and a draft of Andrew Cholewa\'s master\'s thesis, which
provides a thorough description of the language.

## References

\[1\] S. Escobar, C. Meadows, and J. Meseguer. A rewriting-based
inference system for the NRL protocol analyzer and its meta-logical
properties. Theoretical Computer Science, 367(1-2):162-202, 2006. [DOI
link](http://dx.doi.org/10.1016/j.tcs.2006.08.035)

\[2\] S. Escobar, C. Meadows, and J. Meseguer. Equational cryptographic
reasoning in the Maude-NRL protocol analyzer. In Proc. 1st International
Workshop on Security and Rewriting Techniques (SecReT 2006), pages
23-36. ENTCS 171(4), Elsevier, 2007. [DOI
link](http://dx.doi.org/10.1016/j.entcs.2007.02.053)

\[3\] S. Escobar, J. Hendrix, C. Meadows, and J. Meseguer.
Diffie-Hellman cryptographic reasoning in the Maude-NRL protocol
analyzer. In Proc. 2nd International Workshop on Security and Rewriting
Techniques (SecReT 2007), 2007.
[PDF](http://www.dsic.upv.es/%7Esescobar/papers/EscMeaMes-SecReT07.pdf)

\[4\] S. Escobar, C. Meadows, and J. Meseguer. State Space Reduction in
the Maude-NRL Protocol Analyzer. In Proc. of 13th European Symposium on
Research in Computer Security (ESORICS08), LNCS 5283, pages 548-562,
Springer, 2008. [DOI
link](http://dx.doi.org/10.1007/978-3-540-88313-5_35)

\[5\] S. Escobar, C. Meadows, J. Meseguer. Maude-NPA: Cryptographic
Protocol Analysis Modulo Equational Properties. FOSAD 2007/2008/2009
Tutorial Lectures, LNCS 5705, pages 1-50. Springer-Verlag. [DOI
link](http://dx.doi.org/10.1007/978-3-642-03829-7_1)

\[6\] S. Santiago, C. Talcott, S. Escobar, Catherine Meadows, J.
Meseguer. A Graphical User Interface for Maude-NPA. In IX Jornadas sobre
Programacion y Lenguajes (PROLE 2009). Electronic Notes in Theoretical
Computer Science, volume 258, number 1, pages 3-20. Elsevier, 2009. [DOI
link](http://dx.doi.org/10.1016/j.entcs.2009.12.002)

\[7\] S. Escobar, C. Meadows, J. Meseguer, S. Santiago. Sequential
Protocol Composition in Maude-NPA. In Proc. of European Symposium on
Research in Computer Security (ESORICS 2010), LNCS 6345, pages 303-318.
2010. [DOI link](http://dx.doi.org/10.1007/978-3-642-15497-3_19)

\[8\] R. Sasse, S. Escobar, C. Meadows, J. Meseguer. Protocol Analysis
Modulo Combination of Theories: A Case Study in Maude-NPA. In
proceedings of 6th International Workshop on Security and Trust
Management (STM\'10), Lecture Notes in Computer Science, Volume 6710,
pages 163-178, 2011. Download: [DOI
link](http://dx.doi.org/10.1007/978-3-642-22444-7_11)

\[9\] S. Escobar, D. Kapur, C. Lynch, C. Meadows, J. Meseguer, P.
Narendran, and R. Sasse. Protocol Analysis in Maude-NPA Using
Unification Modulo Homomorphic Encryption In proceedings of 13th
International ACM SIGPLAN Symposium on Principles and Practice of
Declarative Programming (PPDP\'2011). Download: [DOI
link](http://dx.doi.org/10.1145/2003476.2003488)

\[10\] S. Erbatur, S. Escobar, D. Kapur, Z. Liu, C. Lynch, C. Meadows,
J. Meseguer, P. Narendran, S. Santiago, and R. Sasse. Effective Symbolic
Protocol Analysis via Equational Irreducibility Conditions. In
proceedings of 17th European Symposium on Research in Computer Security
(ESORICS 2012), LNCS 7459, pages 73-90, 2012. [DOI
link](http://dx.doi.org/10.1007/978-3-642-33167-1_5)

\[11\] S. Erbatur, S. Escobar, D. Kapur, Z. Liu, C. Lynch, C. Meadows,
J. Meseguer, P. Narendran, S. Santiago, and R. Sasse. Asymmetric
Unification: A New Unification Paradigm for Cryptographic Protocol
Analysis. In proceedings of CADE-24 - the 24th International Conference
on Automated Deduction, LNCS 7898, pages 231-248, Springer 2013. [DOI
link](http://dx.doi.org/10.1007/978-3-642-38574-2_16)

\[12\] S. Escobar, C. Meadows, J. Meseguer, S. Santiago State Space
Reduction in the Maude-NRL Protocol Analyzer. Information and
Computation, Volume 238, November 2014, Pages 157-186. [DOI
link](http://dx.doi.org/10.1016/j.ic.2014.07.007)

\[13\] F. Yang, S. Escobar, C. Meadows, J. Meseguer, and P. Narendran.
Theories of Homomorphic Encryption, Unification, and the Finite Variant
Property. In proceedings of 16th International Symposium on Principles
and Practice of Declarative Programming (PPDP 2014), September 8-10,
2014, Canterbury, UK [DOI
link](http://doi.acm.org/10.1145/2643135.2643154)

\[14\] S. Santiago, S. Escobar, C. Meadows, and J. Meseguer. A
Rewriting-based Forwards Semantics for Maude-NPA. In proceedings of
Symposium and Bootcamp on the Science of Security (HotSoS 2014), April
8-9, 2014, Raleigh, NC, USA. [DOI
link](http://dx.doi.org/10.1145/2600176.2600186)

\[15\] S. Santiago, S. Escobar, C. Meadows, and J. Meseguer. A Formal
Definition of Protocol Indistinguishability and its Verification Using
Maude-NPA. In proceedings of 10th International Workshop on Security and
Trust Management (STM 2014), Wrocław, Poland - September 10-11, 2014
LNCS 8743, pages 162-177, Springer 2014. [DOI
link](http://dx.doi.org/10.1007/978-3-319-11851-2)

\[16\] A. González-Burgueño, S. Santiago, S. Escobar, C. Meadows, and J.
Meseguer. Analysis of the IBM CCA Security API Protocols in Maude-NPA.
In proceedings of 1st International Conference on Research in Security
Standardisation (SSR 2014), Royal Holloway, London, UK - December 16-17,
2014 LNCS 8893, pages 111-130, Springer 2014. [DOI
link](http://dx.doi.org/10.1007/978-3-319-14054-4_8)

\[17\] A. González-Burgueño, S. Santiago, S. Escobar, C. Meadows, and J.
Meseguer. Analysis of the PKCS#11 API using the Maude-NPA tool. In
proceedings of 2nd International Conference on Research in Security
Standardisation (SSR 2015). LNCS 9497, pages 86-106. Springer 2015. [DOI
link](http://dx.doi.org/10.1007/978-3-319-27152-1_5)

\[18\] S. Escobar, C. Meadows, J. Meseguer, and S. Santiago. Symbolic
Protocol Analysis with Disequality Constraints Modulo Equational
Theories. In proceedings of Programming Languages with Applications to
Biology and Security - Essays Dedicated to Pierpaolo Degano on the
Occasion of His 65th Birthday. LNCS 9465, pages 238-261. Springer 2015.
[DOI link](http://dx.doi.org/10.1007/978-3-319-25527-9_16)

\[19\] F. Yang, S. Escobar, C. Meadows, J. Meseguer, and S. Santiago.
Strand Spaces with Choice via a Process Algebra Semantics. In
proceedings of 18th International Symposium on Principles and Practice
of Declarative Programming (PPDP 2016). [DOI
link](https://doi.org/10.1145/2967973.2968609)

## Downloads

[Maude-NPA manual v3.1](:maude-npa/Maude-NPA_manual_v3_1.pdf)

[Maude-NPA tool zip file v3.1.4](:maude-npa/Maude-npa-v3_1_4.zip)

Note that Maude-NPA requires a proper installation of
[Maude](https://maude.cs.uiuc.edu), included in the zip file.

## Old versions

* [Maude-NPA tool zip file v3.1.3](:maude-npa/Maude-npa-v3_1_3.zip)
* [Maude-NPA tool zip file v3.1.2](:maude-npa/Maude-npa-v3_1_2.zip)
* [Maude-NPA tool zip file v3.1.1](:maude-npa/Maude-npa-v3_1_1.zip)
* [Maude-NPA v3.1](:maude-npa/Maude-npa-v3_1.zip) ([manual](:maude-npa/Maude-NPA_manual_v3_1.pdf))
* [Maude-NPA v3.0.1](:maude-npa/Maude-npa-v3_0_1.zip) ([manual](:maude-npa/Maude-NPA_manual_v3_0_1.pdf))
* [Maude-NPA v3.0](:maude-npa/Maude-npa-v3_0.zip) ([manual](:maude-npa/Maude-NPA_manual_v3_0.pdf))
* [Maude-NPA v2.0](:maude-npa/Maude-npa-v2_0.zip) ([manual](:maude-npa/Maude-NPA_manual_v2_0.pdf))

## Contact

[Santiago Escobar](https://www.dsic.upv.es/~sescobar/)

[Catherine Meadows](https://www.nrl.navy.mil/itd/chacs/5543)

[José Meseguer](http://cs.illinois.edu/people/faculty/jose-meseguer)

Copyright © 2020, University of Illinois

All rights reserved.
