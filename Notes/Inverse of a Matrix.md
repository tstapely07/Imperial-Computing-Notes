---
date: 2026-01-16
tags:
  - M40017
  - first-year
---
Recall that we can write a [[Systems of Linear Equations|system of linear equations]] as $A\overrightarrow{x}=\overrightarrow{b}$.
Since we know that **multiplication** by the [[Identity Matrix|identity matrix]], has no effect, we can also write:
$$A\overrightarrow{x}=I\overrightarrow{b}$$

If we carry out [[Gaussian Elimination|Gaussian elimination]], by applying the **EROs**, we reach a form:
$$A'\overrightarrow{x}=M\overrightarrow{b}$$
Where $A'$ is in [[Reduced Row Echelon Form|RREF]]. 
If $A'$ is the **identity matrix**, then we in fact have $I\overrightarrow{x}=M\overrightarrow{b}$, or $\overrightarrow{x}=M\overrightarrow{b}$.
From here it is clear to see that $M$ represents the **inverse matrix**.

>[!Summary]
>Essentially we can compute the **inverse** of a matrix using [[Gaussian Elimination|Gaussian elimination]] like so:
>$$\left[\begin{array}{c|c} 
A & I\end{array}\right] \rightarrow EROs\rightarrow
\left[\begin{array}{c|c} 
I & A^{-1}\end{array}\right] $$

