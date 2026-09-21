---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
A **finite state machine** (**FSM**) can represent any [[Synchronous Circuits|synchronous circuit]].
The equations of the **FSM** take the form:
* $S_{t+1}=f(S_t,I_t)$
* $O_{t+1}=g(S_t,I_t)$

Based on their output function $g$, **FSMs** take two different forms.

In a **Mealy machine**, the output logic relies on both the **current state** and the **external inputs**: ^782dff
* ![[Pasted image 20260406195030.png]]
* $f$ is a [[Combinatorial Circuits|combinatorial circuit]], known as the **state sequencing** or **input logic**.
* $g$ is a **combinatorial circuit**, known as the **output logic**.
* $D-Q$ is a set of [[Edge-Triggered D-Type Flip-Flop|flip-flops]] which store the **current state**.

In a **Moore machine**, there is no connection between the input and the **output logic**:
* ![[Pasted image 20260406195222.png]]
* This prevents spikes in $I$ from reaching $g$.

> [!Note]
> **Finite state machines** act as a modelling tool to describe exactly how a **circuit** should behave.

