---
date: 2026-04-14
tags:
  - first-year
  - M40017
---
The suffix "**-morphism**" refers the **structure** of a mathematical **object**.
* In [[40017 - Linear Algebra|linear algebra]], the **objects** are [[vector spaces]], and the **structure** we care about preserving is [[Vectors|vector]] **addition** and **scalar multiplication**.

Let $T:\mathbb{R}^n\to\mathbb{R}^m$ be some [[Linear Transformations|linear transformation]] represented by an $m\times n$ [[Matrices|matrix]] $A$.

A **homomorphism** is a **structure-preserving** mapping.
* Any [[linear mapping]] is a **homomorphism**.

A **monomorphism** is a **homomorphism** that is **injective**:
* No two distinct **vectors** in the **domain** map to the same **vector** in the **codomain**.
* [[Kernel]]: $\operatorname{Ker}(A)=\set{0}$.
* [[Matrix Rank|Rank]]: by [[Rank Nullity Theorem|rank-nullity]], $\operatorname{Rank}(a)=n$.
* [[Image]]: $\dim(\text{Im}(A)) = n$.
* [[Dimension]]: because **rank** cannot exceed the number of **rows**, we have $n\le m$.

A **epimorphism** is a **homomorphism** that is **surjective**:
* **Image**: $\operatorname{Im}(A)=\mathbb{R}^m$ - the image spans the entire **codomain.**
* **Rank**: $m$.
* **Image**: by **rank-nullity**, $\operatorname{dim}(\operatorname{Ker}(A))=n-m$
* **Dimension**: since **rank** cannot exceed the number of **columns**, $m\le n$.

A **isomorphism** is a **homomorphism** that is **bijective**:
* **Kernel**: $\operatorname{Ker}(A)=\set{0}$.
* **Rank**: $\operatorname{Rank}(a)=n$.
* **Image**: $\operatorname{Im}(a)=\mathbb{R}^n$.
* **Dimension**: since $m\le n$ and $n\le m$, we have $n=m$.
* **Determinant**: $\operatorname{det}(A)\neq 0$, so the **matrix** is **invertible**.

An **endomorphism** is a **homomorphism** where the **domain** and **codomain** are the same [[Vector Spaces|space]].
* **Dimension**: since domain and codomain are the same, $m=n$.
* **Rank**: $0\le \operatorname{Rank}(A)\le n$.
* **Image**: $\operatorname{dim}(\operatorname{Im}(A))=\operatorname{Rank}(A)$
* **Kernel**: $\operatorname{dim}(\operatorname{Ker}(A))=n-\operatorname{Rank}(A)$
* **Determinant**: any real number, including $0$.

An **automorphism** is an **endomorphism** that is **bijective**:
* **Dimension**: $n=m$.
* **Kernel**: $\operatorname{Ker}(A)=\set{0}$.
* **Rank**: $\operatorname{Rank}(a)=n$.
* **Image**: $\operatorname{Im}(a)=\mathbb{R}^n$.
* **Determinant**: $\operatorname{det}(A)\neq 0$, so the **matrix** is **invertible**.