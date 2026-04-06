---
date: 2026-03-11
tags:
  - first-year
  - M40017
---
The **Gran-Schmidt process** is an iterative algorithm used to convert any standard basis $\set{\vec{v_1},\vec{v_2},\dots,\vec{v_k}}$ into an [[orthonormal basis]] $\set{\vec{c_1},\vec{c_2},\dots,\vec{c_k}}$.

For the first [[Vectors|vector]], we **normalise** it, by dividing by its magnitude, to obtain the first **unit vector**:
$$\vec{c_1}=\frac{\vec{v_1}}{|\vec{v_1}|}$$
For any subsequent vector $i$, we must first separate it from the [[Vector Subspaces|subspace]] [[Vector Span|spanned]] by all the previously established **orthonormal vectors** ($\operatorname{span}\set{\vec{c_1},\dots,\vec{c_{i-1}}}$).
* 