---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
**Floyd's algorithm** is a modification of [[Warshall's algorithm]] that can efficiently solve **all pairs shortest path problem**: ![[Shortest Path Problem#^74a790]]

Let $G$ be a [[Directed Graphs|directed graph]] with nodes $\{1,\dots,n\}$ and [[Adjacency Matrices|adjacency matrix]] $A$.
Let $B_k[i,j]$ be the length of the **shortest** [[Paths|path]] from $i$ to $j$ which uses **intermediate nodes** $\leq k$.
* If there is no such path, then set $B_k[i,j]=\infty$.
* Base case: clearly $B_0[i,j] = A[i,j]$ if $A[i,j]$ exists, and $\infty$ otherwise.
* Final goal: $B_n[i,j]$ will be the length of the shortest **path** from $i$ to $j$. 

Now we just need to calculate $B_k$ from $B_{k-1}$ (for $k=1,\dots,n$):
* Suppose we have a shortest **path** $p$ from $i$ to $j$ using **intermediate nodes** $\leq k$ of length $d$.
* There are two cases:
	* If $k$ is not an **intermediate node** of $p$, then the shortest path hasn't changed, so we have $B_{k-1}[i,j]=d$ already.
	* If $K$ is an **intermediate node** of $p$:
		* Clearly, $k$ occurs only once, since $p$ is a a shortest **path**.
		* Now we have paths $i$ to $k$ and $k$ to $j$, which use **intermediate nodes** $\leq k-1$.
		* These paths are the shortest **paths** using **intermediate nodes** $\leq k-1$, otherwise $p$ wouldn't be a shortest **path**.
		* So $d=B_{k-1}[i,k]+B_{k-1}[k,j]$.
* Since $\operatorname{min}(x,\infty)=x$, we can simplify this logic to a single line:
	* $B_k[i,j]=\operatorname{min}(B_{k-1}[i,j], B_{k-1}[i,k]+B_{k-1}[k,j])$

Here's an **implementation** of the algorithm in **python-like pseudocode**.
Note:
* The input $A$ is an **adjacency matrix**.
```Python
def floyds(A):
	# initialisation
	for i in range(n):
		for j in range(n):
			if i == j:
				B[i][j]=0
			elif A[i][j] != 0:
				B[i][j] = A[i][j]
			else:
				B[i][j] = +inf
	# end initialisation
	
	for k in range(n):
		for i in range(n):
			for j in range(n):
				B[i][j] = min(B[i][j], B[i][k] + B[k][j])
	
	return B
```

With three nested loops that iterate from $1$ to $n$, the complexity is clearly $O(n^3)$.