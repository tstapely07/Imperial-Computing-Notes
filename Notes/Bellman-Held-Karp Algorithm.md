---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
The **Bellman-Held-Karp** algorithm is a method used to solve the [[Travelling Salesman Problem (TSP)|Travelling Salesman Problem]], and is an example of [[Dynamic Programming|dynamic programming]].

We start with a [[Complete Graph|complete]] [[Weighted Graphs|weighted graph]] $(G,W)$ with [[nodes]] $\{1,\dots,n\}$.
We arbitrarily fix a start node, for instance, node $1$.
For each **node** $x\neq 1$ and each $S\subseteq \operatorname{nodes}(G) \setminus \{1,x\}$:
* Find and store the minimum cost, $C(S,x)$ of a path travelling from node $1$ to node $x$ using precisely the nodes from $S$ as the **intermediate nodes**.

To calculate $C(S,x)$, we do so in increasing order of size:
* We do all $S$ of size $0$, then $1$, up to $n-2$.
* Base case: clearly $C(\phi,x)=W(1,x)$, since no **intermediate nodes** are allowed.
* Inductive step:
	* Assume we know $C(S,x)$ for all $S$ of size $k$.
	* Suppose $|S|=k+1$.
	* Consider the last **intermediate node** $y$ in a least cost path from $1$ to $x$ using **intermediate nodes** $S$.
	* The cost must be $C(S\setminus y, y)+W(y,x)$.
	* So $C(s,x)=min_{y\in  S}(C(S\setminus y, y)+W(y,x))$.


Finding the final solution:
* Let the first **node** be $1$, without loss of generality, and let the last **node** before returning to $1$ be $x$.
* The least cost of such a tour is $C(\operatorname{nodes}(G)\setminus\{1,x\},x)+W(x,1)$.
* So the solution to the **TSP** is $min_{x\neq 1}(C(\operatorname{nodes}(G)\setminus\{1,x\},x)+W(x,1))$

Here's an implementation of the algorithm using **python-like pseudocode**:
* Note that $(G,W)$ is a **weighted graph**.
```Python
def bellman_held_karp((G,W)):
	start = nodes(G)[0]
	for x in nodes(G) \ [start]:
		C[[], x] = weights[start, x]
		
	# process sets S in increasing order of size
	for S in nodes(G) \ [start]:
		if len(S) == 0:
			continue
		for x in (nodes(G) \ S) \ [start]:
			# find C[S,x]
			C[S,x] = +inf
			for y in S:
				C[S,x] = min(C[S \ [y], y] + W[y,x], C[S,x])
	# now we have calculated and stored all values of C[S, x]
	
	opt = +inf
	for x in nodes(G) \ [start]:
		opt = min(C[nodes(G) \ [start, x], x] + W[x, start], opt)
	
	return opt
```

For each subset of **nodes**, we do $O(n^2)$ work with the two nested loops.
There are $2^n$ subsets, so the overall complexity is $O(n^22^n)$.

> [!Note]
> The **Bellman-Held-Karp algorithm** can be adapted to solve the [[Hamiltonian Paths and Circuits|Hamiltonian circuit problem]]. The complexity is still $O(n^22^n)$.