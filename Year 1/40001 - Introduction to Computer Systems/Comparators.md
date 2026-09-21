---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
**Comparators** are used to **compare** [[binary]] numbers.
* i.e. whether $A\gt B$, $A=B$ or $A\lt B$.

Building a $4$ or $8$-**bit** **comparator** requires too many inputs for it to be feasible using [[Karnaugh maps]] or [[Boolean algebra]], so instead we use [[functional design]].

We first build a $1$-**bit** **comparator**:
* ![[Pasted image 20260409160836.png|402]]

If we add an **enable** input, we will be able to change these comparators together.
* Note that the $A\lt B$ is also redundant, since we can calculate is using a NOR [[Logic Gates|gate]].
Here is our new **building block**:
* ![[Pasted image 20260409160941.png|409]]
We can now build a **comparator** of any size, such as this $4$-**bit** **comparator**:
* ![[Pasted image 20260409161010.png|484]]
