---
date: 2026-04-21
tags:
  - first-year
  - M40018
---
Recall that our **interpretation** of the [[Hoare Triples|Hoare triple]]:
$$\set P\quad \text{code}\quad\set Q$$
Is "if property $P$ holds before the execution of `code`, then after the execution of `code` property $Q$ will hold".
* However, if `code` never terminates, then we have nothing to prove.

To prove **partial correctness** we must show that if the **code** is executed in a **state** satisfying its [[Pre-Conditions and Post-Conditions|pre-condition]], then if it **terminates** it must reach a **state** that satisfies its **post-condition**.

To prove **total correctness** we must prove **partial correctness**, and also prove that the **code** will **terminate**.

