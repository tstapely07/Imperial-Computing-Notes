---
date: 2026-04-17
tags:
  - first-year
  - M40005
---
Due to its origins as a $16$-[[Binary|bit]] **architecture**, a **word** in [[x86]] refers to a $16$-**bit** **datatype**.
* $32$-**bit** quantities are **double** **words**, and $64$-**bit** quantities are **quad** **words**.

**Assembly** **instructions** are given a **suffix**, to identify the datatype they yare working on, as given by this table:
* ![[Pasted image 20260417213609.png|492]]
* Note that `char*` is written as an example, but this generalises to all **pointers**.

> [!Note]
> We will focus on **integer operations**, and so generally we need only consider `b`, `w`, `l` and `q`.