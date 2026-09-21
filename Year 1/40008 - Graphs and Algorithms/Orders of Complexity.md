---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
When [[Algorithm Analysis|analysing]] the **worst case complexity** $W(n)$ of an algorithm, we care most about how the algorithm behaves as the input size $n$ gets very large.

As $n$ gets large, the highest power of $n$ becomes the most important term, and we can ignore constant factors and lower terms:
* If $W(n)=8n^2+300n+70$, we say the algorithm is **order** $n^2$.
* If $W'(n)=2n^3+n^2+4$, it is **order** $n^3$.
Algorithms with a **lower order** should always be preferred for large $n$, so we would chose $W(n)$ here, even though $W'(n)\lt W(n)$ for small $n$.

In practice, when calculating **time complexity**, choosing what specific operation to count, e.g. just expensive multiplications, vs multiplication and additions, only changes the constant factors, not the overall order:
* For $n\times n$ [[Matrices|matrix multiplication]], counting both gives $W(n)=n^2(2n-1)=2n^3-n^2$.
* Counting only multiplications gives $W(n)=n^3)$.
* But we can ignore the factors, and get the same **order**, $n^3$.
* For this reason, we ignore the constant factors, for easier comparison.

We generally rank algorithms by their **order**, the two main categories are:
* **Polynomial**: $1,n,n^2,n^3\dots$
* **Exponential**: $2^n, 3^n, 4^n, \dots$
We are also interested in **logarithms**, for example the **worst case complexity** of [[binary search]] is **order** $\log n$.
* We can interleave **logarithmic factors** into the **polynomial hierarchy**:
* $1,\; \log n,\; n,\; n \log n,\; n^2,\; n^2 \log n\dots$
