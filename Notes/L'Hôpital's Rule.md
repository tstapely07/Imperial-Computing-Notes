---
date: 2026-04-07
tags:
  - first-year
  - M40016
---
If we are evaluating a [[Limits|limit]] of a ratio of two **functions**, $\lim_{x\to a} \frac{f(x)}{g(x)}$, and direct substituting yields an [[Indeterminate Forms|indeterminate form]], such as $\frac{0}{0}$, then we can apply **L'Hôpital's rule**:
$$\lim_{x\to a} \frac{f(x)}{g(x)}=\lim_{x\to a} \frac{f'(x)}{g'(x)}$$

> [!Example]
> For example, $\lim_{x\to0} \frac{\sin x}{x}$.
> Direct substitution yields $\frac{sin(0)}{0}=\frac{0}{0}$.
> But **L'Hôpital's rule** gives:
> $$\lim_{x\to 0} \frac{\sin x}{x}=\lim_{x\to 0} \frac{\cos x}{1}$$
> Now we can substitute, to get $\frac{\cos 0}{1}=\frac{1}{1}=1$, and so:
> $$\lim_{x\to 0} \frac{\sin x}{x}=1$$
> 

> [!Tip]
> **L'Hôpital's rule** can be applied multiple times, if after applying it once, we are still left with an **indeterminate form**.