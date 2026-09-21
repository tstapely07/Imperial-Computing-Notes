---
date: 2026-01-28
tags:
  - first-year
  - M40008
---
As an example:
* ![[Pasted image 20260128162017.png|300]]
	* Arbitrarily start at $1$.
	* Fan out to visit **adjacent** [[Nodes|nodes]] at distance $1$ - $2$ and $8$.
	* Then visit **nodes** at distance $2$ - $3$, $4$, and $7$.
	* Finally visit $5$ and $6$.
* Final order of visiting - `1,2,8,3,4,7,5,6`.
* As expected, we obtain a [[Spanning Trees|spanning tree]], but a different one to what [[Depth-First Search (DFS)|DFS]] gave us.

**BFS** is naturally expressed using a **FIFO queue** of **nodes**.
* The **queue** is initialised with start node $x$.
* We process **nodes** from the **front** of the **queue**.
* For each **node**, we visit its immediate neighbours, adding them to the **back** of the **queue**.
Here is **python-like pseudocode** for **BFS**.
Note that:
* The [[Graphs|graph]] is stored as an [[Adjacency Lists|adjacency list]].
* `visited` is a Boolean array of **nodes**, initialised with every element as `False`.
* `parent` is the [[Node Parent|parent]] node in the search [[Trees - Graphs|tree]].
* Nodes are outputted in the order visited.
```Python
q = Queue()
def bfs(x):
	visited[x] = True
	print(x)
	enqueue(x, Q)
	while not isEmpty(Q):
		y = dequeue(Q)
		for z in adj[y]:
			if not visited[z]:
				visited[z] = True
				print(z)
				parent[z] = y
				enqueue(z, Q)
```

The **queue** grows and shrinks during the computation.
The size of the **queue** represents the "breadth" of the front on which the **BFS** is working.
As with [[Depth-First Search (DFS)|DFS]], each **node** is processed once, and each [[Adjacency Lists|adjacency list]] is processed once.
* This again results in $O(n+m)$.

**BFS** gives the shortest path from the **start node** to any reachable **node**, while **DFS** may give a longer distance than necessary.
* The shortest path from a **node** $y$ to the start node can be found as:
	*  `y, parent[y], parent[parent[y]],... , start`