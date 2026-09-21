---
date: 2026-04-05
tags:
  - first-year
  - M40008
---
When [[Algorithm Analysis|analysing]] and algorithm's **time complexity** based on an input size of $n$, we look at the number of **comparisons**.
* The number of **comparisons** often varies depending on the specific input.

There are two types of analysis:
>[!Abstract]  Definition
>**Worst case analysis** - $W(n)$ - the **largest** number of comparisons for any input of size $n$.

>[!Abstract]  Definition
>**Average case analysis** - $A(n)$ - the **average** number of comparisons for any input of size $n$.

Note that **average case analysis** requires knowing, or assuming, the probability distribution of the inputs.

We generally prefer **worst case analysis**.
* It provides a **strict guarantee** that the algorithm will never take longer than $W(n)$ on input size $n$.
* $W(n)$ is generally much easier to compute than $A(n)$.
* **Worst case** and **average case** analysis tend to yield similar results, with the same **order of complexity.**

>[!Note]
>We generally avoid **best case analysis**, since a slow algorithm can appear fast on specific inputs.


