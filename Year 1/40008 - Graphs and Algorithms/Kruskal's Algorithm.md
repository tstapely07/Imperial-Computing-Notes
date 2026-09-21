---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
[[Prim's Algorithm|Prim's algorithm]] was [[Greedy Algorithms|greedy]], by always choosing the shortest candidate arc.
* This turned out to give optimal results.

**Kruskal's algorithm** is even more **greedy**:
* At each stage, choose the shortest [[Arcs|arc]] not yet included, except when this would give a [[Cycles|cycle]].

For example:
* ![[Pasted image 20260204150118.png|400]]

At intermediate stages we get a [[Forest|forest]], rather than a [[Trees - Graphs|tree]].

The algorithm goes as follows:
	$F=\emptyset$
	$R = arcs(G)$
	while $R$ nonempty:
		remove $a$ of smallest weight from $R$
		if $a$ does not make a cycle when added to $F$:
			add $a$ to $F$
	return F

**Arcs** are added in increasing order of [[Weighted Graphs|weight]].

Let $G$ be a **connected weighted graph**.
To prove **correctness**, we show that at each stage $k$, we have forest $F_k\subseteq T'$. where $T'$ is an **MST** of $G$.
* This proof is in the lecture notes.

To implement the algorithm we have to do two things:
* Look at each **arc** in ascending order of weight.
	* We can use a [[Priority Queues|priority queue]] here.
* Check whether adding the **arc** to the **forest** so far creates a **cycle**.
	* We can use **dynamic equivalence classes**.
	* We put **nodes** in the same **equivalence class** if they belong to the same [[Connected Components|connected component]] of the **forest** constructed so far.
	* We map each **node** to the representative of its **equivalence class**.
	* An arc $(x,y)$ can be added if $x$ and $y$ belong to different equivalence classes.
	* If $(x,y)$ is added, then **merge** the equivalence classes of $x$ and $y$.

**Dynamic equivalence classes** can be handled using the [[Union-Find Datatype|Union-Find datatype]].

The implementation goes as follows:
* First we let $G$ have $n$ nodes numbered from $1$ to $n$.
* Then we build a priority queue $Q$ of the edges of $G$ with the weights as keys.
```Python
sets = UFcreate(n)
F = []
while not isEmpty(Q):
	(x,y) = getMin(Q)
	delteMin(Q)
	x` = find(sets,x)
	y` = find(sets,y)
	if x` != y`: # no cycle
		F.add(x,y)
		union(sets,x`,y`)
```

Now let's consider the complexity.
* There will be $O(m)$ inserts to the build the **priority queue** - taking time $O(m\;log\;m)$ 
* $O(m)$ `getMin` and $O(m)$ `deleteMin` - taking time $O(m\;log\;m)$.
* $O(m)$ `find` - taking time $O(m\;log\;n)$.
* $O(n)$ `union` - taking time $O(n)$.
So the overall time taken is $O(m\;log\;m)$, assuming $m\geq n$, as is normally the case.
In fact, the number of **arcs** $m$ is bounded by $n^2$, so $O(m\;log\;m)$ = $O(m\;log\;n)$.
* So the overall complexity is $O(m\;log\;n)$, which is the same as [[Prim's Algorithm#Prim's Algorithm with Priority Queues|Prim's algorithm with a priority queue]].

We can build the **priority queue** in time $O(m)$ rather than $O(m\;log\;m)$, but this doesn't affect the overall complexity.

If we improve the **union-find** using [[Union-Find Datatype#^b009cd|path compression]], the complexity for that part then reduces to $O((n+m)\;log^*\;n)$
* Here, $log^*\;n$ is an extremely slow-growing function.
* $log^*\;n\leq5$ for any conceivable $n$.