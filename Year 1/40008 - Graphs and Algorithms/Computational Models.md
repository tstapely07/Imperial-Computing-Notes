---
date: 2026-04-07
tags:
  - first-year
  - M40008
---
Different models can measure **input size** or **computation steps** differently:
* In sorting a list, the **input size** is the length of the list, and we counted **computation steps** as comparisons, ignoring all other **computation steps**.
* In the [[Euler Paths and Circuits|Euler]] [[Paths|path]] problem, the **input size** was measured either using [[adjacency matrices]] or [[adjacency lists]], and the **computation steps** involve inspecting the input and incrementing counters.

> [!Abstract] Definition
> If a problem can be solved in [[Class P|p-time]] in some **reasonable model**, then it can be solved in **p-time** in **any other reasonable model**.
> * Note that this could be a different **polynomial**.

There are some **unreasonable models** that violate this:
* **Superpolynomial parallelism** allows us to carry out more than **polynomially** many operations simultaneously.
	* This could solve **exponential time** problems in **p-time**, so it is **unreasonable**.
* **Unary numbers**, such as representing $5_{10}$ as $11111_1$ give an input size that is **exponentially** larger than any other base, making an **exponential time** **algorithm** appear **p-time**.
	* For example, checking if a number is prime takes $n$ divisions, which appears to be **p-time** in **unary**, since the input size is $n$.
	* However, the **input size** for a number is actually $\log n$, making this an **exponential time** algorithm.
