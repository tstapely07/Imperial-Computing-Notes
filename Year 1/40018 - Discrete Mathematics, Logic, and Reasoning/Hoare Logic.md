---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
**Hoare logic** is a way to formally reason directly with [[Hoare triples]].
There is an **axiom** for dealing with assignment:
$$\frac{P[x\mapsto x_{old}]\wedge x=E[x\mapsto x_{old}]\longrightarrow Q}{\{P\}\quad x=E\quad\{Q\}}$$
Note that $P[x\mapsto y]$ means to replace all **free** occurrences of $x$ with $y$.
* In this case, we are replacing all occurrences of $x$ with references to the variable's old value $x_{old}$ in both the [[Pre-Conditions and Post-Conditions|precondition]] and the **assignment expression**.