---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
**Warshall's algorithm** defines an **efficient** method for computing the [[Transitive Closure and Directed Graphs|transitive closure]] of a [[directed graphs|directed graph]]. 

Suppose the [[nodes]] are $\{1,\dots,n\}$.
Consider a [[paths|path]] $p=x_1,x_2,\dots,x_k$.
* We say that **nodes** $x_2,\dots,x_{k-1}$ are **intermediate nodes** of **path** $p$.


We looks for **paths** which use **nodes** $\leq i$ as **intermediate nodes**.
* Let $B_k[i,j]$ iff there is a **path** from $i$ to $j$ which uses **intermediate nodes** $\leq k$, otherwise set $B_k[i,j]=0$.
* Recall we defined: ![[Transitive Closure and Directed Graphs#^6cd841]]
* Base case: clearly $B_0[i,j]=A[i,j]$, since we only have **paths** of length one, and there can be no **intermediate nodes** $\leq 0$.
* Final goal: $R^+(i,j)$ iff $B_n[i,j]=1$, since $B_n$ allows all possible **intermediate nodes**, and so all **possible paths**.

Now we just need to calculate $B_k$ from $B_{k-1}$, for $k=1,\dots,n$.
* Suppose we have a path from $i$ to $j$ using **intermediate nodes** $\leq k$.
* There are two cases:
	* If $k$ is not an **intermediate node** of $p$, then $B_{k-1}[i,j]$ already.
	* If $k$ is an intermediate node of $p$:
		* We can assume that $k$ only occurs once. if it did occur multiple times we could simple shorten the **path** by removing the [[Cycles|cycle]] from $k$ to $k$.
		* We can split the path from $i$ to $j$ into two **paths**, $i$ to $k$ and $k$ to $j$, both of which use **intermediates nodes** $\leq k-1$.
		* So we have $B_k[i,j]$ if we already have $B_{k-1}[i,k]$ and $B_{k-1}[k,j]$.

We can write an implementation using **python-like pseudocode**.
Note:
* $A$ is an [[Adjacency Matrices|adjacency matrix]].
* The returned $B$ is the **transitive closure**.
```Python
def warshalls(A):
	B = copy(A)
	for k in range(n):
		# at the start of the loop, B represents B_{k-1}
		for i in range(n):
			for j in range(n):
				B[i][j] = B[i][j] or (B[i][k] and B[k][j])
		# at the end of the loop, B represents B_k
	return B
```

With three nested loops that iterate from $1$ to $n$, the complexity is clearly $O(n^3)$.