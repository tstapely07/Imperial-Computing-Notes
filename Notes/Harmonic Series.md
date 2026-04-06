---
date: 2026-03-26
tags:
  - first-year
  - M40016
---
The **harmonic series** is defined as $\sum_{n\ge1} \frac{1}{n}$.
Clearly, as $n\to\infty$, $a_n\to0$, however the **series** **diverges**.
Proof:
$$\sum_{n=1}^{\infty} \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} + \dots$$
Let us now consider that:
* $\frac{1}{2}=\frac{1}{2}$
* $\frac{1}{3}+\frac{1}{4}\gt \frac{1}{4}+\frac{1}{4}=\frac{1}{2}$
* $\frac{1}{5}+\frac{1}{6}+\frac{1}{7}+\frac{1}{8}\gt 4\left( \frac{1}{8} \right)=\frac{1}{2}$
* The next $8$ terms will be $\gt 8\left( \frac{1}{16} \right)=\frac{1}{2}$
We can then establish that:
$$S_{2^n}\gt 1+\frac{n}{2}$$
So clearly $(S_n)_{n\ge1}$ **diverges**, and so the **harmonic series** also **diverges**.

