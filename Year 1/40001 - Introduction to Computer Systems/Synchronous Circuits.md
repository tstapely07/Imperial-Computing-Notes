---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
> [!Abstract] Definition
> A **synchronous circuit** is a type of [[Sequential Circuits|sequential circuit]] that will settle to the correct value after some **defined** amount of time.
> * This is controlled by a **clock signal**.

Virtually all **synchronous digital systems** follow the same model, consisting of three distinct blocks:
* ![[Pasted image 20260406155812.png|378]]
* The **state memory** is a bank of [[Edge-Triggered D-Type Flip-Flop|edge-triggered D-type flip-flops]] all wired to the same [[Clocks|clock]], to store the **current state** of the system.
	* This can be thought of as a [[binary]] number, with one **bit** stored by each **flip-flop**.
* The **state sequencing logic** is a [[Combinatorial Circuits|combinatorial circuit]] that takes the **current state** and an external input, and computes the next state.
	* $D_k=F_k(I_1,I_2,\dots I_n,Q_1,Q_2,\dots Q_m)$.
	* Also recall that the **flip-flop's** output at time $t+1$ is equal to its input at time $t$:
		* $Q_k(t+1)=D_k(t)$
* The **output logic** is another **combinatorial circuit** that calculates the final outputs based on the **current state**.
	* $O_j=G_j(Q_1,Q_2,\dots,Q_m)$

> [!Note]
> The **clock speed** is limited by the **time delay** of the **state sequencing logic** in the worst case.



