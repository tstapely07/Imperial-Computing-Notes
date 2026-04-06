---
date: 2026-01-28
tags:
  - first-year
  - M40008
---
As an example:
* ![[Pasted image 20260128161630.png|300]]
	* Arbitrarily start at $1$.
	* Go to $2$ and start **DFS** from $2$.
	* Backtrack from $3$ to $2$, and then go to $4$.
	* At $8$ all **adjacent** [[Nodes|nodes]] are visited, backtrack to start.
* Final order of visiting - `1,2,3,4,5,6,7,8`.
* As expected, we obtain a [[Spanning Trees|spanning tree]].

**DFS** uses **recursion**, for each node $y$, we perform **DFS** completely at $y$, before backtracking to the parent node $x$.
Here is **python-like pseudocode** for **DFS**.
Note that:
* The [[Graphs|graph]] is stored as an [[Adjacency Lists|adjacency list]].
* `visited` is a Boolean array of **nodes**, initialised with every element as `False`.
* `parent` is the [[Node Parent|parent]] node in the search [[Trees - Graphs|tree]].
* Nodes are outputted in the order visited.
```Python
def dfs(x):
	visited[x] = True
	print(x)
	for y in adj[x]:
		if not visited[y]:
			parent[y] = x
			dfs(y)
			# backtrack to x
```

`dfs(x)` is applied to each node **exactly once** if the **graph** is [[Connectedness|connected]].
Each application of `dfs(x)` runs through the [[Arcs|arcs]] incident on `x` exactly once.
The running time of **DFS** is therefore $O(n+m)$, where $n$ is the number of **nodes**, and $m$ is the number of **arcs**.