---
date: 2026-02-10
tags:
  - first-year
  - M40008
---
# Outline
**Dijkstra's algorithm** is very similar to [[Prim's Algorithm|Prim's algorithm]], and is used to solve the [[Shortest Path Problem|single pair shortest path problem]].

As in **Prim's**, we build up a [[Spanning Trees|spanning tree]] starting from the `start` node.
We classify [[Nodes|nodes]] into:
* **Tree nodes** - already included.
* **Fringe nodes** - not yet included but adjacent to a **tree node**.
* **Unseen nodes** - all other nodes.

We have already computed the shortest path from `start` to all the **tree nodes** - it is the path given by the **tree**.
We also know the shortest path to the **fringe nodes** so far, but this may improve as the **tree** grows.

For example:
* ![[Pasted image 20260210153104.png|300]]
* Now we update $3$ by adding it's **candidate arcs**.
* ![[Pasted image 20260210153123.png|300]]
* Now `distance[2]=10` and `distance[4]=7`, so we add $4$ to the **tree**.
* ![[Pasted image 20260210153204.png|300]]
* Now we add $2$ to the **tree**.
* ![[Pasted image 20260210153223.png|300]]
* Now we add $5$ to the **tree**.
* ![[Pasted image 20260210153238.png|300]]
* Now `distance[6]` has reduced to `16`, so we add $6$ and $7$.
* ![[Pasted image 20260210153328.png|300]]

Although we computed paths to **all nodes** from `start`, we usually stop as soon as `finish` joins the **tree**.
Note that we obtained a spanning tree, but it was not necessarily an [[Minimum Spanning Trees|MST]].

# Implementation
We store two values for each **tree** or **fringe node**:
* It's [[Node Parent|parent]] **node** in the [[Trees - Graphs|tree]].
* The **distance** of the shortest path known.

At each stage, the next **node** to be added to the **tree** is the **fringe node** with the smallest **distance**.
We then update the fringe, possibly improving the current shortest path.
We can obtain the shortest path to a node `x` in reverse order from the `parent` function: `x, parent[x], parent[parent[x]],..., start`

The input is a **weighted graph** $(G, W)$, together with a pair of nodes `start, finish`.
The output will be the length of the shortest path from **start** to **finish**.
Here's the **python-like pseudocode**:
```Python
def dijkstras((G,W), start, finish):
	# initialisation
	tree[start] = True
	for x in adj[start]:
		# add x to fringe
		fringe[x] = true
		parent[x] = start
		distance[x] = W(start, x)
	# end of initialisation
	
	while not tree[finish] and fringe nonempty:
		# select f s.t. distance[f] is minimum
		fringe[f] = False
		tree[f] = True
		for y in adj[f]:
			if not tree[y]:
				if fringe[y]:
					# update distance and candidate arc
					if distance[f] + W(f, y) < distance [y]:
						distance[y] = distance[f] + W(f,y)
						parent[y] = f
				else:
					# y is unseen
					fringe[y] = True
					distance[y] = distance[f] + W(f, y)
					parent[y] = f
					
	return distance[finish]
```
Once the algorithm has terminated, we can read off the path, using `parent`.
It runs in $O(n^2)$, just like **Prim's algorithm**.

# Correctness
The algorithm clearly **terminates**, since the tree grows each execution of the while loop.
To prove **correctness**, we need to formulate an **invariant**.

Invariant:
1. If `x` is a **tree** or **fringe node**, other than`start`, then `parent[x]` is a **tree node**.
2. If `x` is a **tree node**, other than `start`, then `distance[x]` is the length of the shortest path, and `parent[x]` is its predecessor along that path. 
3. If `f` is a **fringe node**, then `distance[f]` is the length of the shortest path where all nodes, except `f`, are **tree nodes**. Also, `parent[f]` is its predecessor along that path.
	* ![[Pasted image 20260210160403.png|200]]

When the program terminates, `finish` is a **tree node**, so by (2) we then have the required shortest path.
So we must show that the invariant is:
* Established before the while loop.
* Maintained during the while loop.

Proving (2) is maintained:
* Suppose `f` is added to the **tree**.
	* We need to check that we have found the shortest path.
* The path given by the algorithm is `start,...,parent[f],f`.
* Suppose we have a different, shorter path, $P$, that is not necessarily in the **tree**.
	* Let `y` be the first node on $P$ not to belong to the **tree**.
	* By (3), `distance[y] <= distance from start to y via P`
	* Hence `length of P >= distance[y]`
	* But `distance[y] >= distance[f]` by our choice of `f`.
	* Combining these gives `length of P >= distance[y] >= distance[f]`.
	* So `length of P >= path(f)`.
* ![[Pasted image 20260210161240.png|200]]
The remainder of the proof is omitted for brevity.

# Optimisation with Priority Queues
Much like we optimised **Prim's** algorithm with a [[priority queues|priority queue]], we can do the same for **Dijkstra's**.
The implementation goes as follows:
```Python
# initialisation
def dijkstras((G,W), start, finish):
	Q = PQcreate()
	for x in nodes(G):
		key[x] = +inf
		parent[x] = null
		insert(Q, x)
	decreaseKey(Q, start, 0)
	# end initialisation
	
	while not tree[finish] and not isEmpty(Q):
		f = getMin(Q)
		deleteMin(Q)
		tree[f] = True
		for y in adj[f]:
			if not tree[y]:
				# y in Q
				if key[f] + W(f, y) < key[y] :
					decreaseKey(Q, y, key[f] + W(f, y))
					parent[y] = f
	
	return key[finish]
```

# Analysis
Once again, the analysis is very similar to that of **Prim's algorithm**.
With a **PQ** implemented with a **binary heap**, the overall complexity is $O(m\;log\;n)$, assuming $n<m$ as is usually true.
With a **PQ** implemented with a **Fibonacci heap**, the overall complexity is $O(m+n\;log\;n)$