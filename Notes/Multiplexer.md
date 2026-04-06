---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
A **multiplexer** acts as a digital switch.
* The simplest **multiplexer** takes two inputs, $A$ and $B$, and a third control input, $C$.
* The output is as follows:
$$R+\begin{cases}A\quad\text{ if } C=0\\B\quad\text{ if } C=1\end{cases}$$
* We can construct one out of [[logic gates]] like this:
	* ![[Pasted image 20260405200358.png|351]]

**Multiplexers** can also take more than 2 inputs, with sufficiently many control inputs to select between them.
* $n$ control inputs can choose between $2^n$ inputs.

