---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
Just like we annotate [[Variables in Proofs|variables]], we must also annotate **arrays**, and their contents.
For example, to prove:
$$\set{a[k]=0}\quad\text{a[k]=a[k]+5}\quad\set {a[k]=5}$$
We would need to show that:
$$a[k]_{old}=0\land a[k]=a[k]_{old}+5\;\longrightarrow\; a[k]=5$$
Note that the position of $\__{old}$ matters:
* ![[Pasted image 20260420195635.png|528]]

Like any other variable, we can also annotate the array reference itself, while this is rarer:
* ![[Pasted image 20260420195708.png|494]]
