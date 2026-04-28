---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
**Locality** states that **programs** tend to use **data** or **instructions** with [[x86 Memory Layout|memory addresses]] near or equal to those they have used recently.
* This principle is divided into two rules.

**Temporal locality** states that recently referenced items are likely to be referenced again in the near future.

**Spatial locality** states that items with nearby addresses tend to be referenced close together in time.

For example, here's a `for` [[x86 Loops|loop]]:
```C
sum = 0;
for (i=1; i<n; i++) {
	sum += a[i];
} 
return sum;
```
* Examples of **temporal locality** are updating the `sum` variable every iteration, and executing the same **instructions** in the **loop** multiple times.
* Examples of **spatial locality** are iterating through an [[x86 Arrays|array]] sequentially (a **stride**-$1$ **pattern**), and the **instructions** being naturally arranged sequentially in **memory**.

> [!Example]
> Here is an example of **bad spatial locality**, since we end up with a **stride** of $N$:
> * ![[Pasted image 20260420164747.png|506]]
> Flipping the **loops** gives much better **spatial locality**, now a **stride** of $1$:
> * ![[Pasted image 20260420164814.png|511]]

> [!Tip]
> Good **locality** results in better [[x86 Cache|cache]] [[performance]].