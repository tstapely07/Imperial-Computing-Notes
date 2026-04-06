---
date: 2026-03-10
tags:
  - first-year
  - M40017
---
Since $-1\le \cos\theta\le1$ the [[inner product]] of two [[Vectors|vectors]] is bounded by their **magnitudes**:
$$-|\vec{a}||\vec{b}|\le \vec{a}\cdot \vec{b}\le|\vec{a}||\vec{b}|$$
Squaring both sides yields:
$$(\vec{a}\cdot \vec{b})^2\le(\vec{a}\cdot \vec{a})(\vec{b}\cdot \vec{b})$$
* Note that $\vec{a}\cdot\vec{a}=|\vec{a}|^2$.

The **inequality** is only equal when $\cos\theta=\pm 1$, so $\theta=0\degree$ or $\theta=180\degree$.
* This is when the two vectors are [[Linear Independence|linearly dependent]], so $\vec{a}=k\vec{b}$.


Here's one **application** of the **inequality**:
Let $k_1,k_2,\dots,k_n$ be positive real numbers.
Then:
$$(k_1+k_2+\dots+k_n)(\frac{1}{k_1}+\frac{1}{k_2}+\dots+\frac{1}{k_n})\ge n^2$$
We can prove this by constructing the following [[vectors]], and substituting into the squared **Cauchy-Schwarz** inequality:
$$a=\begin{bmatrix}\sqrt{k_1}\\\sqrt{k_2}\\\vdots\\\sqrt{k_n}\end{bmatrix},b=\begin{bmatrix}\frac{1}{\sqrt{k_1}}\\\frac{1}{\sqrt{k_2}}\\\vdots\\\frac{1}{\sqrt{k_n}}\end{bmatrix}$$
* This gives $a\cdot b=1+1+\dots+1$, or $a\cdot b=n$, giving us the $n^2$.
* The other side of the equation follows clearly.