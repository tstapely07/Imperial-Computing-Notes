---
date: 2026-02-10
tags:
  - first-year
  - M40008
---
# Outline
Another algorithm for the [[Shortest Path Problem#^b70e51|single pair shortest path problem]] is the **A\*** .
We assume that we have a [[Heuristic Function]] function $h(x)$.

> [!Example]
> If we were dealing with cities on a map, $h$ could be the **Euclidean distance**.

Each **node** has:
* $g(n)$ - the cost to reach that node from `start`.
* $h(n)$ - the **heuristic function** of that node.
* $f(n)=g(n)+h(n)$

Let's trace an example:
* Here, each node $x$ has its **heuristic value** $h(x)$ shown in red.
* ![[Pasted image 20260210163409.png|400]]
* First we add `start` to the tree.
* ![[Pasted image 20260210163449.png|400]]
* Now we pick the **node** with the lowest **f-score**, in this case $B$, with $3+7=10$.
* ![[Pasted image 20260210164129.png|400]]
* Now the lowest **f-score** belongs to $C$, with $(3+5)+3=11$.
* ![[Pasted image 20260210164218.png|400]]
* Now the lowest **f-score** is tied between $D$, with $(3+5+4)+0=12$, and $H$, with $2+10=12$. Let's arbitrarily pick $H$.
* ![[Pasted image 20260210164356.png|400]]
* Now the lowest **f-score** belongs to $D$, with the same $(3+5+4)+0=12$.
* ![[Pasted image 20260210164424.png|400]]
* And `finish` has been reached.

# Implementation
We input a [[Weighted Graphs|weighted graph]] $(G, W)$ together with a pair of nodes `start`, `finish`, and a **consistent heuristic function** $h$.
The output will be the length of the shortest path from `start` to `finish`.
Here's the **python-like pseudocode**:
```Python
def aStar((G, W), start, finish, h):
	#initialisation
	tree[start] = True
	g[start] = 0
	f[start] = g[start] + h[start]
	for x in adj[start]:
		fringe[x] = True
		parent[x] = start
		g[x] = W[start, x]
		f[x] = g[x] + h[x]
	# end initialisation
	
	while not tree[finish] and fringe nonempty:
		# select a fringe node s.t. f[x] is minimum
		fringe[x] = False
		tree[x] = True
		for y in adj[x]:
			if not tree[y]:
				if fringe[y]:
					#update g(y), f(y), and candidate arc
					if g[x] + W(x, y) < g(y):
						g[y] = g[x] + W(x, y)
						f[y] = g[y] + h[y]
						parent [y] = x
				else:
					# y is unseen
					fringe[y] = True
					g[y] = g[x] + W(x, y)
					f[y] = g[y] + h[y]
					parent[y] = x
	return g[finish]
```

Let us make note of a few details:
* The set of **tree nodes** is often called the **closed set** and the set of **fringe nodes** is the **open set**.
* If we set $h(x)=0$ for all nodes $x$, then $h$ is **consistent**, and the **A\*** algorithm is just [[Dijkstra's Algorithm|Dijkstra's algorithm]].
* In the worst case, the running time for **A\*** is the same as **Dijkstra's** but we hope to do better on average, depending on the **heuristic function**.
* There is a more general version of **A\*** that is guaranteed to give the correct solution for **admissible heuristics**, rather than just **consistent heuristics**. 
	* Here, we also need to re-examine [[Nodes|nodes]] that are already in the **tree**.

# Correctness
Proving correctness will be very similar to how we did so for **Dijkstra's**.
The algorithm terminates, since the **tree** clearly grows each iteration of the while loop.
To prove **correctness**, we need an **invariant**.

Invariant:
1. If `x` is a **tree** or **fringe node**, other than`start`, then `parent[x]` is a **tree node**.
2. If `x` is a **tree node**, other than `start`, then `distance[x]` is the length of the shortest path, and `parent[x]` is its predecessor along that path. 
3. If `f` is a **fringe node**, then `distance[f]` is the length of the shortest path where all nodes, except `f`, are **tree nodes**. Also, `parent[f]` is its predecessor along that path.
	* ![[Pasted image 20260210160403.png|200]]

As in **Dijkstra's**, when the program terminates, `finish` is a **tree node**, and by (2) we have the shortest path.
So we just need to show that the invariant is:
* Established before the while loop.
* Maintained during the while loop.

Proving (2) is maintained:
* Suppose `x` is added to the **tree**.
	* We need to check that we have found the shortest path.
* The path given by the algorithm - `start,...,parent[x],x` has length `g(x)`
* Suppose we have a different and shorter path `P`, not necessarily in the **tree**.
	* Then `len(P) < g[x]`
	* Let `y` be the first **node** on `P` not to belong to the **tree**.
	* Let `P1` be `P` from `start` to `y`, and let `P2` be from `y` to `x`.
	* `f[y] = g[y] + h[y]` 
	* `<= g[y] + len(P2) + h[x]` - by **consistency of** of `h`.
	* `<= len(P1) + len(P2) + h[x]` - by (3) for `y`.
	* ` = len(P) + h(x)`
	* `<g[x] + h[x]` - by assumption.
	* But `f[x] <= f[y]` by our choice of `x`, so we have a **contradiction**.

# Optimisation with Priority Queues
We can optimise the **A\*** algorithm with **priority queues**:
```Python
def aStar((G, W), start, finish, h):
	# initialisation
	Q = PQcreate()
	for x in nodes(G):
		g[x] = +inf
		key[x] = +inf
		parent[x] = nil
		insert(Q, x)
	g[start] = 0
	decreaseKey(Q, start, g[start]+h[start])
	# end initialisation
	
	while not tree[finish] and not isEmpty(Q):
		x = getMin(Q)
		deleteMin(Q)
		tree[x] = True
		for y in adj[x]:
			if not tree[y]:
				# so y in Q
				if g[x] + W(x, y) < g[y]:
					g[y] = g[x] + W(x, y)
					decreaseKey(Q, y, g[y]+h[y])
					parent[y] = x
	
	return g[finish]
```