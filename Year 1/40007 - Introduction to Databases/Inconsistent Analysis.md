---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
An **inconsistent analysis anomaly** occurs when a [[Transactions|transaction]] calculates a **summary**, like a **sum**, while another **transaction** is halfway through moving data around.
* $T_1$ reads $x$ and $y$ to compute a **summary**, but after $T_1$ reads $x$, $T_2$ transfers a value between $x$ and $y$. When $T_1$ then reads $y$, it reads the new value, and so the **summary** is incorrect.

[[Serialisability and Recoverability|Serialisable histories]] never suffer from **inconsistent analysis**.
* Note that a **history** with a **inconsistent analysis** can still be **recoverable**.

> [!Example]
> Here's an example where **inconsistent analysis** occurs:
> * ![[Pasted image 20260414103507.png|495]]