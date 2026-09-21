---
date: 2026-03-11
tags:
  - first-year
  - M40017
---
An **orthogonal projection** takes a [[Vectors|vector]] in a **higher-**[[Dimension|dimensional]] [[Vector Spaces|space]], and finds the closest possible **vector** in a **lower-dimensional** [[Vector Subspaces|subspace]].

Let $U$ be a **subspace** of $\mathbb{R}^n$ with dimension $k$:
$$U=\operatorname{span}\set{\vec{b_1},\vec{b_2},\dots,\vec{b_k}}$$
We then define an $n\times k$ [[Matrices|matrix]] $B$ by placing the [[Basis of a Subspace|basis]] **vectors** of $U$ as the **columns:
$$B=\begin{bmatrix}\vec{b_1}&\vec{b_2}&\dots&\vec{b_k}\end{bmatrix}$$

The **orthogonal projection matrix** $P_U$ onto the **subspace** $U$ is then:
$$P_U=B(B^\top B)^{-1}B^\top$$

Given an arbitrary **vector** $x\in \mathbb{R}^n$:
* $P_U\vec{x}$ is the **vector** in the **subspace** $U$ closest to $\vec{x}$.
* The **error vector**, the difference between the original **vector** and its **projection**, is strictly **perpendicular** to the **subspace** $U$:
$$(\vec{x}-P_U\vec{x})\perp \vec{b_i}\quad\forall i\in\set{1,2,\dots,k}$$
