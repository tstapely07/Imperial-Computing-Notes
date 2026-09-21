---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
**Armstrong's axioms*** are the three core rules about [[functional dependencies]].
Here, $X,Y,Z$ are sets of [[attributes]], and as standard, $XY$ is a shorthand for $X\cup Y$.

**Reflexivity** states that:
$$Y\subseteq X\models X\to Y$$
* This is known as a **trivial FD**.
> [!Example]
> If $amount$ and $tdate$ are **attributes**, then:
> $$\begin{gather}amount,tdate\to amount\\\text{and}\\amount,tdate\to tdate\end{gather}$$

**Augmentation** states that:
$$X\to Y\models XZ\to YZ$$
> [!Example]
> If $no,cname,sortcode$ are **attributes** and $no\to cname$, then:
> $$no,sortcode\to cname,sortcode$$

**Transitivity** states that:
$$X\to Y, Y\to Z\models X\to Z$$

> [!Example]
> If $no\to sortcode$ and $sortcode\to bname$ then:
> $$no\to bname$$
