---
date: 2026-02-20
tags:
  - first-year
  - M40017
---
**Linear transformations** are [[Linear Mapping|linear mappings]] that move [[vectors]], and so **transform** the entire **domain** space.
Geometrically, transformations include:
* Stretching.
* Shearing.
* Rotating.
* Projecting down to a [[Dimension|lower-dimensional]] [[Vector Spaces|space]].
* Embedding into a **higher-dimensional** **space**.

In fact, **linear transformations** and **linear mappings** are equivalent.

Just like there is a [[Matrix Representation of Linear Mappings|matrix representation]] for every **linear mapping**, we can also represent a **transformation** as a **matrix**.

For the [[standard ordered basis]], the **matrix columns** are simply the images of the **standard basis vectors**. 
We can generalise this for any pair of [[Ordered Basis|bases]]:
* Let $B$ be a **basis** of the **domain** **vector space** $\mathbb{R}^n$, and let $F$ be a **basis** of the **codomain vector space** $\mathbb{R}^m$.
* If $\Phi_{FB}:\mathbb{R}^n\to\mathbb{R}^m$ is a **linear transformation**, then we can obtain its **transformation matrix** as $\Phi_{FB}=\begin{bmatrix}\Phi(b_1) & \Phi(b_2) & \dots & \Phi(b_n)\end{bmatrix}$
* Here $b_1,b_2,\dots,b_n$ are the **basis vectors of** $B$, i.e. $b_{1\,w.r.t\,B}=\begin{bmatrix}1\\0\\\vdots\\0\end{bmatrix}$
We can represent the same **linear transformation** $\Phi_{FB}$ in different **bases** too:
Let $C$ be another **basis** of $\mathbb{R}^n$ and $G$ be another basis of $\mathbb{R}^m$.
Now we can easily obtain:
* $\Phi_{GB}=I_{GF}\Phi_{FB}$
* $\Phi_{FC}=\Phi_{FB}I_{BC}$
* $\Phi_{GC}=I_{GF}\Phi_{FB}I_{BC}$

There are some **key differences** between a [[basis change]] and a **linear transformation**:
* A **basis change matrix** must be square, but a **linear transformation matrix** can be any shape.
* A **basis change matrix** must be invertible, but the same does not apply to a **linear transformation matrix**.
* From the **basis change** perspective, the **vector space** isn't being transformed, we are only looking at it from a different perspective. A **linear transformation** of course does **transform** the **vector space**.

We can **visualise** the effect a **transformation** has on the $\mathbb{R}^n$ **space** in three ways:
* **Basis change** - what happens to the [[standard ordered basis]].
* **Determinants** - how the n-dimensional **volume** of a **unit cube** is scaled.
* [[Eigenspaces]] - how the space is stretched, sheared, or flipped along specific directional axes.
