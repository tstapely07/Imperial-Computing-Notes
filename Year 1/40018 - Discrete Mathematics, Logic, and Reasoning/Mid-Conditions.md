---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
A [[Pre-Conditions and Post-Conditions|pre-condition]] and a [[Pre-Conditions and Post-Conditions|post-condition]] alone aren't enough to reason about a **sequence** of state-changing statements.
* We implement **mid-conditions**, to act as checkpoints in the code.
For example:
```Code
// Pre: P
code1
// Mid: R
code2
// Post: Q
```
Now the logical rule is:
$$\frac{\set P\quad \text{code1}\quad\set R\quad\set R\quad \text{code2}\quad\set Q }{\set P\quad \text{code1 ; code2} \quad\set Q}$$

For example, here's a program with many **mid-conditions**:
* ![[Pasted image 20260420201115.png|389]]
* Note how we must keep track of $a$, $b$, and $c$ throughout the program, even on steps they aren't directly needed, since they will be needed for later steps.
From these **mid-conditions** we get the following **informal proof obligations**:
* ![[Pasted image 20260420201224.png|482]]
Which become the following **formal logical assertions**:
* ![[Pasted image 20260420201251.png|485]]
