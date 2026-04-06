---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
# Outline
**Prim's algorithm** is one way to find a [[Minimum Spanning Trees|minimum spanning tree]] of a [[Graphs|graph]].

It requires a starting [[Nodes|node]].
At each step, we added the shortest [[Arcs|arc]] that will extend the [[Trees - Graphs|tree]].
For example:
* ![[Pasted image 20260204132558.png|400]]
* Here the **arcs** are added in the order:
	* $(1,2)$
	* $(1,4)$ or $(2,3)$
	* $(4,3)$

> [!Note]
> This is a [[Greedy Algorithms|greedy]] approach.

At an arbitrary stage in **Prim's algorithm**, there are three kinds of [[Nodes|nodes]]:
* **Tree nodes** - nodes in the tree.
* **Fringe nodes** - nodes adjacent to a tree node, making them candidates to join the tree at the next stage.
* **Unseen nodes** - all other nodes.
Initially, all nodes are **unseen**, since the **tree** is empty.

The algorithm logic goes as follows:
	Choose any node $start$ as the **root**
	Reclassify $start$ as a **tree**
	Reclassify all nodes adjacent to $start$ as **fringe**
	while **fringe** nonempty:
		Select an arc of minimum weight between a **tree node** $t$ and a **fringe node** $f$
		Reclassify $f$ as **tree**
		Add the arc $(t,f)$ to the tree
		Reclassify all unseen nodes adjacent to $f$ as **fringe**

For $n$ **nodes** and $m$ **arcs**, the while loop is execute $O(n)$ times.
Selecting the arc of **minimum weight** involves finding the shortest **arc** among all possible **arcs** between $O(n)$ **tree nodes** and $O(n)$ **fringe nodes**.
* So this is $O(n+m)$
The whole algorithm is therefore $O(n(n+m))$.

# Optimising with Candidate Arcs
For one improvement, we can keep track of the **candidate arcs** - the **arcs** that might be used.
For example:
* Initially we just have $1$ in the **tree**, with **fringe nodes** $2,3,4$:
	* ![[Pasted image 20260204135424.png|400]]
* Now $(1,2)$ is added, the **fringe nodes** are $3,4$, and the **candidate arc** for $3$ has changed:
	* ![[Pasted image 20260204135501.png|150]]
* Now $(1,4)$ is added, the only **fringe node** is $3$, and the **candidate arc** for $3$ has changed again:;
	* ![[Pasted image 20260204135607.png|150]]
This functionality can be implemented using a **parent** function, like we did for [[Traversal Algorithms|graph traversal]]:
* Initially `parent[3]=1`
* Then `parent[3]=2`
* Finally `parent[3]=4`
Let the **parent** of a **fringe node** $f$ be the **tree node** $t$ such that $(t,f)$ has the **least weight**.

Now we can write some **python-like pseudocode**:
* We choose any **node** `start` as the **root**.
```Python
# initialise tree
tree[start] = true
# initialise fringe
for x in adj[start]:
	# add x to fringe
	fringe[x] = true
	parent[x] = start
	weight[x] = W[start,x]
# end of initialisation

while fringe nonempty:
	# select f s.t. weight[f] is minimum
	fringe[f] = false
	tree[f] = true
	for y in adj[f]:
		if not tree[y]:
			if fringe[y]:
				# update candidate arc if lower weight is possible
				if W[f, y] < weight[y]:
					weight[y] = W[f,y]
					parent[y] = f
			else:
				# y is unseen - add to fringe
				fringe[y] = true
				weight[y] = W[f,y]
				parent[y] = f
```
As before, there are $O(n)$ executions of the while loop.
When executing the while loop:
* Testing whether the fringe is empty is $O(n)$.
* Finding the fringe node $f$ such that `weight[f]` is minimum is $O(n)$.
* The updating of the candidate arc for each `y in adj[f]` is $O(1)$, making the for loop $O(n$).
So the algorithm is $O(n^2)$:
* This improves on our earlier version that was $O(n(n+m))$, especially considering that $m$ could be as large as $n^2$, which would cause $O(n(n+m))$ to be $O(n^3)$.

# Correctness
Let $G$ be a **connected weighted graph** with $n$ **nodes**.
Let the **trees** constructed at each stage by $T_0, \dots, T_k,\dots$.
$T_0$ is just the node $start$.
$T_{k+1}$ is obtained from $T_k$ by adding some **arc** $a_{k+1}$.
$T_k$ has $k+1$ **nodes**.
There are $n-1$ stages, with $T_{n-1}$ being returned by the algorithm.

We will show by induction on $k$ that each $T_k$ is a [[Subgraphs|subgraph]] of an **MST** $T'$ of $G$.

The **base case** is $k=0$. $T_0$ has one **node** and no **arcs**.
Clearly $T_0\subseteq T'$ for any **MST** $T'$ of $G$.

For the **induction step**, assume that $T_k\subseteq T'$. for some **MST** $T'$ of $G$.
![[Pasted image 20260204142246.png|200]]
If $a_{k+1}\in\operatorname{arcs}(T')$ then $T_{k+1}\subseteq T'$ as required.
Suppose $a_{k+1}\not\in\operatorname{arcs}(T')$
	Since $T'$ is a **spanning tree** there must be a path in $T'$ from $x$ to $y$, and this path must cross from $T_k$ to the **fringe**, as shown in this diagram:
		![[Pasted image 20260204142449.png|400]]
	So we form a new **spanning tree** $T''$ from $T'$ by removing $a$ and adding $a_{k+1}$.
	Since the algorithm chose $a_{k=1}$ rather than $a$, we have $W(a_{k+1})\leq W(a)$.
	Hence $W(T'')\leq W(T')$, and so $T''$ is an **MST**.
		In fact, since all **MSTs** have the same weight, $W(a_{k+1})= W(a)$.
	Also $T_{k+1}\subseteq T''$ has required.
	This completes the **induction step**.
	Now $T_{n-1}$ has $n-1$ **arcs**, and $T_{n-1}\subseteq T'$ for some **MST** $T'$.
	Since all **spanning trees** for $G$ have $n-1$ **arcs**, we must have $T_{n-1}=T'$.
	Hence $T_{n-1}$ is an **MST** as required.

We can regard the **induction hypothesis** as an **invariant**. 
This is something that is:
* Established initially.
* Maintained through each execution of the while loop of the code.
We can also note:
* Each $T_k$ constructed by **Prim's algorithm** is [[Connectedness|connected]].
* $T_k$ is an **MST** for the [[Subgraphs|subgraph]] of $G$ **induced** by $nodes(T_k)$:
	* The subgraph with **nodes** $nodes(T_k)$ and all **arcs** of $G$ which join **nodes** in $nodes(T_k)$.
But these two notes are not required for the proof.

# Prim's Algorithm with Priority Queues
Each item `x` of the queue has a priority `key[x]`, which is usually a natural number.
* The key represent the cost.
* Items are removed lowest key first.
The operations available to us include:
* `PQcreate()`
* `isEmpty(Q)`
* `insert(Q,x)`
* `getMin(Q)`
* `deleteMin(Q)`
* `decreaseKey(Q,x,newkey)` - updates `key[x] = newkey`.

Let's rewrite **Prim's algorithm**, using priority queues:
```Python
Q = PQcreate()
for x in nodes(G):
	key[x] = +inf
	parent[x] = null
	insert(Q,x)
decreaseKey(Q, start, 0)

while not isEmpty(Q):
	f = getMin(Q)
	deleteMin(Q) # these two lines are like dequeueing
	tree[f] = true
	for y in adj[f]:
		if not tree [y]: # so y in Q
			if W[f,y] < key[y]:
				decreaseKey(Q,y,W[f,y])
				parent[y] = f
```
Here's a diagrammatic **trace** of the algorithm:
* ![[Pasted image 20260204143712.png|450]]

With $n$ **nodes** and $m$ **arcs**, the number of priority queue operations is:
* $O(n)$ inserts.
* $O(n)$ empty checks.
* $O(n)$ get mins.
* $O(n)$ delete mins.
* $O(m)$ decrease keys.
In a good implementation of a **priority queue**, via a **binary heap**, all operations are $O(log(n))$, bar `isEmpty` and `getMin` which are $O(1)$.
So Prim's algorithm with a **priority queue** is overall $O(m\cdot log(n))$, assuming that $n<m$, as is usually the case.

We an also implement a **priority queue** with **Fibonacci heaps** rather than **binary heaps**. Now, all operations are $O(1)$, apart from `deleteMin`, which is $O(log(n))$.
Now the complexity of **Prim's**, with a **Fibonacci heap priority queue** is $O(m+n\;log\;n)$, although in practice the memory usage and constant factors can be high.

# Comparison
If a **graph** is [[Sparse Graph|sparse]], say $m\leq n \cdot log(n)$:
* $O(m\; log\;n)\simeq O(n\; log^2\;n)$
* Which is better than $O(n^2)$.
* So the priority queue implementation is better.

If a **graph** is **dense**, say $m\simeq n^2$:
* $O(m\; log\;n)\simeq O(n^2\; log\;n)$
* Which is worse than $O(n^2)$.
* So the classic implementation is better.
