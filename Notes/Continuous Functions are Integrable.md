---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
> [!Theorem]
> If a function $f:[a,b]\to\mathbb{R}$ is [[Continuity|continuous]], then $f$ is **integrable** on $[a,b]$.

Proof:
To show $f$ is **integrable**, we must show that the difference between its **upper sum** and **lower sum** can be made arbitrarily small, so let $\epsilon \gt 0$.
Because $f$ is **continuous** on a **closed** and **bounded** **interval**, it is [[Uniform Continuity|uniformly continuous]], therefore there exists some $\delta\gt 0$ such that for any two points $x,y\in[a,b]$:
$$|x-y|\lt \delta\implies |f(x)-f(y)|\lt \frac{\epsilon}{b-a}$$
* Note that we can pick $\frac{\epsilon}{b-a}$, since we can pick any $\epsilon\gt0$.
Now we choose any **partition** $P$, where $||P||\lt \delta$.
On any **closed subinterval** $[r_{i-1}-r_i]$, the [[extreme value theorem]] guarantees that $f$ attaints its **supremum** $M_i$ and **infimum** $m_i$.
* Now, since $|r_{i}-r_{i-1}\lt\delta$, we can guarantee that $M_i-m_i\lt \frac{\epsilon}{b-a}$.
Now lets consider $S^u(f,P)-S^l(f,P)$:
$$\begin{gather}
S^u(f,P)-S^l(f,P)=\sum_{i=1}^n(r_i-r_{i-1})M_i-\sum_{i=1}^n(r_i-r_{i-1})m_i\\
\\=\sum_{i=1}^n(r_i-r_{i-1})(M_i-m_i)\\
\lt \sum_{i=1}^n(r_i-r_{i-1})\left( \frac{\epsilon}{b-a} \right)\\
=\frac{\epsilon}{b-a}\sum_{i=1}^n(r_i-r_{i-1})
\end{gather}$$
The **sum** of the **subinterval** widths $\sum_{i=1}^n(r_i-r_{i-1})$ is simply the total width, $(b-a)$, and so have:
$$\begin{gather}
S^u(f,P)-S^l(f,P)\lt\frac{\epsilon}{b-a}(b-a)\\
S^u(f,P)-S^l(f,P)\lt \epsilon
\end{gather}$$
So for any $\epsilon\gt 0$, we can find some **partition** where $S^u(f,P)-S^l(f,P)\lt\epsilon$.
* Because the **upper sum** and **lower sum** can be forced arbitrarily close to each other, the **upper integral** and **lower integral** must be exactly equal.
* Therefore $f$ is **integrable**.