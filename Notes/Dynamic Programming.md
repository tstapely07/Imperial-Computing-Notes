---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
In **dynamic programming**:
* The **main problem** is broken down into **sub-problems**.
* The **sub-problems** are then ordered, e.g. by increasing size, with the final **sub-problem** being the original **main problem**.

To solve the **main problem**:
* Move through the **sub-problems** in order.
* Solve each **sub-problem** using the stored solutions of the previous **sub-problems**, and storing the new solution for later use.
* Solve the **main problem** as the final **sub-problem**.

Two examples of **dynamic programming** are [[Warshall's algorithm]] and [[Floyd's algorithm]].
