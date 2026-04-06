---
date: 2026-03-22
tags:
  - first-year
  - M40016
---
The standard **triangle inequality** states that:
$$|a+b| \le |a|+|b|$$

The proof is simple:
We know by the definition of absolute values that:
$$\begin{gather}-|a|\le a\le |a|\\
-|b| \le b \le |b|\end{gather}$$
By adding these inequalities, we obtain:
$$-(|a|+|b|)\le a+b \le |a|+|b|$$
This perfectly matches the definition of absolute value for the term $(a+b)$ so we can conclude that:
$$|a + b| \le |a| + |b|$$


The **reverse triangle inequality** states that:
$$|a-b| \ge ||a|-|b||$$
We obtain this by starting with $a=(a-b)+b$, and applying the standard **triangle inequality** to the right hand side:
$$|a|=|(a-b)+b|\le |a-b|+|b|$$
Now we just subtract $|b|$ from both sides:
$$|a|-|b|\le |a-b|$$
Since the variables are **arbitrary** we also have:
$$|b|-|a| \le |b-a|$$
Now from here:
$$\begin{gather}
|b|-|a|\le |a-b|\\
-(|a|-|b|)\le|a-b|
\end{gather}$$
Because both $(|a|-|b|)$ and $-(|a|-|b|)$ are $\le |a-b|$, we can conclude:
$$||a|-|b||\le |a-b|$$
