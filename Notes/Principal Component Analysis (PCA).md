---
date: 2026-03-11
tags:
  - first-year
  - M40017
---
**Principle component analysis** is a [[Dimension|dimensionality]] reduction technique.
* It uses the [[Covariance|covariance]] [[Matrices|matrix]] to find the most important "axes" of a dataset.
* This means that when we project it to fewer dimensions, we minimise the information lost.

First we [[Diagonalisation|diagonalise]] the **covariance matrix**:
$$[\operatorname{cov}]=PDP^{-1}$$
* Here, $P$ is constructed from the [[Eigenvectors and Eigenvalues|eigenvectors]] of $\text{cov}$ and $D$ is constructed from the corresponding **eigenvalues**.
We now sort the **eigenvectors** in $P$ so that their corresponding **eigenvalues** are in descending order: $(\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n)$
* The [[Eigenspaces|eigenspace]] of the **largest** **eigenvalue**, $E_{\lambda_1}=\operatorname{span}(\vec{v}_{\lambda_1})$, is the **1st principle component**.
	* Also, the **eigenvalue** $\lambda_1$ is the **variance** along $E_{\lambda_1}$.
* Similarly, the **eigenspace** $E_{\lambda_2}=\operatorname{span}(\vec{v}_{\lambda_2})$ is the **2nd principle component**.
To reduce the data to $k$ **dimensions**, we simply create a subspace $U$ [[Vector Span|spanned]] by the first $k$ principle components:
$$U=\operatorname{span}\set{\vec{v_{\lambda_1}},\vec{v_{\lambda_2}},\dots,\vec{v_{\lambda_k}}}$$
We then construct the [[orthogonal projection matrix]] $P_U$ using these $k$ **eigenvectors** as the columns of $B$, with $P_U=B(B^\top B)^{-1}B^\top$.
* Then we map every single datapoint $\vec{w_i}$ to $P_U\vec{w_i}$.

When we compress data, we lose information.
* The loss for a single datapoint is the distance between the **original vector** and its new **projected vector**:
	* $d(\vec{w_i},P_U\vec{w_i})=||\vec{w_i}-P_U\vec{w_i}||$
The **total projection error** is the sum of these errors across the entire dataset:
$$\text{TPE} = \sum_{i=1}^n d(\vec{w}_i, P_U\vec{w}_i)$$
