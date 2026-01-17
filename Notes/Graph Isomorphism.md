---
date: 2026-01-16
tags:
  - first-year
  - M40008
---
![[Pasted image 20260116161447.png|200]]
These two [[Graphs|graphs]] look different, but we can see that the [[Nodes|nodes]] are connected in the same way.
If we take $1\mapsto B,2\mapsto A, 3\mapsto D, 4\mapsto C$, then we have a **bijection** between the **nodes**.
* We need to check that the connections are the same.
* Although it is trivial in this case, to check rigorously, we need to use [[Adjacency Matrices|adjacency matrices]].

In the standard order, ($1234$ and $ABCD$), the adjacency matrices are:
$$
\begin{pmatrix}0 & 2 & 0 & 2 \\
2 & 0 & 1 & 1 \\
0 & 1 & 0 & 1 \\
2 & 1 & 1 & 0
\end{pmatrix}
\;\;
\begin{pmatrix}
0 & 2 & 1 & 1 \\
2 & 0 & 2 & 0 \\
1 & 2 & 0 & 1 \\
1 & 0 & 1 & 0
\end{pmatrix}
$$
If we reorder the right-hand matrix to correspond to the mapping $1\mapsto B,2\mapsto A, 3\mapsto D, 4\mapsto C$, like we had before, we obtain:
$$
\begin{array}{ccccc} 
  & B & A & D & C \\
B & 0 & 2 & 0 & 2 \\
A & 2 & 0 & 1 & 1 \\
D & 0 & 1 & 0 & 1 \\
C & 2 & 1 & 1 & 0
\end{array}
$$
Now we it is clear that the graphs are **isomorphisms**.

> [!Abstract] Definition
> If $G$ and $G'$ are [[Graphs|graphs]], then an **isomorphism** from $G$ to $G'$ is a bijection $f:nodes(G)\rightarrow nodes(G')$ together with a bijection $g:arcs(G)\rightarrow arcs(G')$ such that if $a\in arcs(G)$ has endpoints $n_1$ and $n_2$, then the endpoints of $g(a)$ are $f(n_1)$ and $f(n_2)$.
> * This is equivalent the **adjacency matrices** of $G$ and $G'$ being the same, except that the rows and columns may have been reordered.

To test for **isomorphism**, we first start with the most obvious checks:
* Number of [[Nodes|nodes]].
* Number of [[Arcs|arcs]].
* Number of loops.
* Number of [[Degrees|degrees]].

In general, discovering whether two graphs are **isomorphic** has quite a **high complexity**.
We need to see whether the **adjacency matrices** are rearrangements of each other.
For $n$ nodes, there are $n!$ rearrangements.

>[!Info]
A special case of an **isomorphism** is an [[Graph Automorphism|automorphism]].
