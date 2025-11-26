---
title: Applications
---

Maude and its formal tools have been used in many pioneering applications:

* Formal definition and verification of programming and hardware, resp. software, modeling languages:
  full C ([ER12](https://doi.org/10.1145/2103621.2103719)),
  Java ([FCMR04](https://doi.org/10.1007/978-3-540-27813-9_46)),
  JVM ([FMR04](https://doi.org/10.1007/978-3-540-27815-3_14)),
  [NASA's PLEXIL](https://shemesh.larc.nasa.gov/fm/PLEXIL/)
    ([RCMS12](https://doi.org/10.1007%2F978-3-642-30729-4_24)),
  Verilog ([MKMR10](https://doi.org/10.1109/MEMCOD.2010.5558634)),
  E-LOTOS ([V02](https://doi.org/10.1007%2F3-540-36135-9_19),
    [VM05](https://doi.org/10.1007/s10703-005-2254-x)),
  UML ([CE06](https://doi.org/10.1007%2F11784180_28),
    [DRMA14](https://doi.org/10.1007/978-3-642-54624-2_11)),
  MOF ([BM10](https://doi.org/10.1007/s00165-009-0140-9)),
  ODP ([DV03](https://doi.org/10.1016/S0920-5489(02)00121-6),
    [DRV05](https://doi.org/10.1016/j.csi.2004.10.008),
    [RVD07](https://doi.org/10.1016/j.csi.2006.11.004)),
  AADL ([OBM10](https://doi.org/10.1007/978-3-642-13464-7_5),
    [BOM14](https://doi.org/10.1007/978-3-319-06410-9_7)),
  Ptolemy ([BOFLT14](https://doi.org/10.1016/j.scico.2010.10.002)),
  BPMN ([DS17](https://doi.org/10.1007/978-3-319-59746-1_12),
    [DRS18](https://doi.org/10.1016/j.scico.2018.08.007),
    [DMC23](https://doi.org/10.1007/978-3-031-12441-9_6),
    [DPR24](https://doi.org/10.1016/j.jlamp.2023.100928)),
  DSMLs ([RRDV](https://doi.org/10.5381/jot.2007.6.9.a10),
    [RDV09](https://doi.org/10.1177/0037549709341635),
    [D23](https://doi.org/10.5381/jot.2022.21.4.a2)),
  Multi-Level Modelling Languages ([RMDRW23](https://doi.org/10.1016/j.jlamp.2022.100831),
    [RDK23](https://doi.org/10.1007/s10270-021-00947-1)).

* Semantics of hardware architectures: MCA ARMv8 architecture
    ([XZ22](https://doi.org/10.1016/j.sysarc.2022.102438)).

* Browser security: uncovering 12 kinds of unknown attacks on Internet Explorer
    ([CMSWW07](https://doi.org/10.1109/SP.2007.6)),
  and design and verification of the secure-by-construction Illinois's IBOS browser
    ([SKMT12](https://doi.org/10.1007/978-3-642-35861-6_14),
    [SMR20](https://doi.org/10.1007%2F978-3-030-63595-4_10)).

* Cryptographic protocol analysis:
  [Maude-NPA](tools/maude-npa) has analyzed many protocols and crypto-APIs modulo algebraic properties, like
    Yubikey&YubiHSM ([GAEMM18](https://easychair.org/publications/paper/qkkq)),
    IBM's CCA ([GSEMM14](https://doi.org/10.1007/978-3-319-14054-4_8)),
    and PCKS#11 ([GSEMM15](https://doi.org/10.1007/978-3-319-27152-1_5)),
  using unification and symbolic reachability. See [EMM09](https://doi.org/10.1007/978-3-642-03829-7_1). An account of the NRL protocol analyzer can be found [here](https://doi.org/10.1016/j.tcs.2006.08.035). [Tamarin](https://tamarin-prover.github.io/) at ETH, resp. [AKISS](https://github.com/akiss/akiss) at INRIA, use Maude's     unification to analyze protocols like 5G-AKA ([DC18](https://people.cispa.io/cas.cremers/tamarin/5G/)), resp. RFID ([GK17](https://doi.org/10.1007/978-3-319-66399-9_1)).

* Networks: AER/NCA active networks ([OKMTZ06](https://doi.org/10.1007/3-540-45314-8_24)),
  MANETS ([LOM16](https://doi.org/10.1016/j.jlamp.2015.05.002)),
  BGP ([Wetal13](https://repository.upenn.edu/cgi/viewcontent.cgi?article=2029&context=cis_reports),
  [Wetal11](https://doi.org/10.1007/978-3-642-21461-5_22),
  [WTGLS12](https://doi.org/10.1007/978-3-642-28756-5_20));
  DDoS-Intruder models; and DDoS protection ([LDFN18](https://doi.org/10.1016/j.jlamp.2017.09.001)):
  ASV ([AMG09](https://doi.org/10.1016/j.entcs.2009.02.069)),
  Stable Availability ([EMMW12](http://doi.org/10.1007/978-3-642-28872-2_6)),
  VoIP-SIP ([SASGM09](https://doi.org/10.1007/978-3-642-04444-1_24)), using [Maude's statistical model checking (SMC) tool](https://maude.cs.uiuc.edu/tools/pvesta/).
  Secure bandwidth reservation in path-aware Internet architectures ([WLSPB22](https://zenodo.org/record/5856306#.YgTkifXMLt0)),
  end-to-end name resolution ([LDHBVBP23](https://doi.org/10.1145/3603269.3604870)).
  SCION's bandwidth allocation protocol ([CLBHHMP22](https://doi.org/10.1007/978-3-031-05288-0)).


* Cloud transaction system formalization and analysis:
  Cassandra ([LNGRG15](https://doi.org/10.1007/978-3-319-22264-6_15)),
  Google's Megastore ([GO14](https://doi.org/10.1007%2F978-3-319-10431-7_12)),
  P-Store ([O17](https://doi.org/10.1007/978-3-319-72044-9_13)), etc.
  ([Betal18](https://doi.org/10.1002/9781119428497.ch2)), using SMC.

* Analysis of real-time and cyber-physical systems:
  CASH scheduling ([OC06](https://doi.org/10.1007/11693017_26)),
  sensor ([OT09](https://doi.org/10.1016/j.tcs.2008.09.022))
  and MANET ([LOM16](https://doi.org/10.1016/j.jlamp.2015.05.002)) networks,
  timed security protocols ([AEMMS20](https://doi.org/10.1007%2F978-3-030-65277-7_7)),
  PALS transformation from synchronous to correct distributed real-time systems ([MO12](http://doi.org/10.1016/j.tcs.2012.05.040),
    [BMO12](https://doi.org/10.1007/978-3-642-35861-6_1))
  enables model checking of complex models such as AADL and Ptolemy
  models ([BOM14](https://doi.org/10.1007/978-3-319-06410-9_7))
  and distributed control of airplane maneuvers ([BKMO12](http://doi.org/10.4204/EPTCS.105.2)).


* Models of cell signaling used to explain drug effects, identify pathogen attack surfaces, etc. ([Pathway Logic](http://pl.csl.sri.com/)).
  See [EKLLMS02](https://pubmed.ncbi.nlm.nih.gov/11928493/).

* Specification and analysis of models of Concurrency:
  Petri Nets ([SMO01](https://doi.org/10.1007/3-540-45541-8_9)),
  CCS, pi-Calculus ([S00](https://doi.org/10.1016/S1571-0661(05)80125-2)),
  Actors ([M93](https://mitpress.mit.edu/books/research-directions-concurrent-object-oriented-programming)),
  REO ([MSA](https://doi.org/10.1016/j.entcs.2005.12.034)),
  Orc ([AM15](https://doi.org/10.1016/j.jlamp.2015.03.003)).

* Logical framework applications to prototype logics and build and interoperate theorem provers:
  Barendregt's lambda-cube ([SM04](https://doi.org/10.1007/978-3-540-39993-3_16)),
  linear logic ([MM02](https://doi.org/10.1007/978-94-017-0464-9_1)),
  modal logics ([OPR18](https://doi.org/10.1007/978-3-319-99840-4_7)),
  computational algebraic geometry, Maude's Church-Rosser Checker and Inductive
  ([DM12](https://doi.org/10.1016/j.jlap.2011.12.004),
  [DMR20](https://doi.org/10.1016/j.jlamp.2019.100513)) and Reachability Logic
  ([SSM17](https://doi.org/10.1007/978-3-319-94460-9_12)),
  theorem provers, HOL-to-Nuprl translator ([NSM01](https://doi.org/10.1007/3-540-44755-5_23)),
  integration of logic and deep-learning, etc. These applications use meta-level, search, and symbolic features.

* Distributed databases: SNOW-Optimal Read Atomic Transactions
  ([L22](https://hdl.handle.net/20.500.11850/511821)),
  Replicated RAMP Transactions ([LL21](https://doi.org/10.1109/TASE52547.2021.00026)).

* IoT systems: Attack Surface of Trigger-Action IoT Platforms
  ([WDYLBG19](https://doi.org/10.1145/3319535.3345662)),
  Automated Composition, Analysis and Deployment of IoT Applications
  ([DG19](https://doi.org/10.1007/978-3-030-29852-4_21)).

* Runtime verification: See works by [Roşu and Havelund](https://doi.org/10.1007/s10515-005-6205-y).

Please, help us to complete this page. If you know of applications that should be in this list, email us to `duran(at)lcc(dot)uma(dot)es`.
