---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
Some **proof obligations** present a problem when dealing with **variables**.
For example, in this [[Hoare Triples|Hoare triple]]:
$$\set{0\le x\le 10}\quad \text{x++}\quad\set{0\le x\le 10}$$
We might try and show that:
$$0\le x\le 10\land x=x+1\;\longrightarrow\;0\le x\le 10$$
However, $x=x+1$ is always false, and $false\longrightarrow\text{anything}$ is always true.
* Clearly, this isn't actually the proof we want to construct.

To make things clear, we will use the following notation:
* $x$ will always refer to the most recent value of $x$, i.e. after the code has executed.
* $x_{old}$ will refer to the value of $x$ before the code is executed.
So now, to prove:
$$\set{0\le x\le 10}\quad \text{x++}\quad\set{0\le x\le 10}$$We actually would need to show that:
$$0\le x_{old}\lt 10\land x=x_{old}+1=0\le x\le 10$$
Note that we will only use $\__{old}$ when a variable is actually modified, to simplify our proves.
For example, to prove:
$$\set{x=1\land y=2}\quad \text{x=x+y}\quad\set{x=3\land y=2}$$
We would only annotate $x$, like so:
$$x_{old}=1\land y=2\land x=x_{old}+y\;\longrightarrow\;x=3\land y=2$$
