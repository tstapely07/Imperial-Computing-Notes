---
date: 2026-01-28
tags:
  - first-year
  - M40008
---
Given a list of tasks to be completed, where some tasks must be completed before others, we can view this as a [[Directed Graphs|directed graph]]:
* ![[Pasted image 20260128164826.png|300]]
* The [[Graphs|graph]] must be [[Cycles|acyclic]], or else a possible order to complete the tasks does not exist.

The problem is, given a [[Directed Graphs|directed]], **acyclic** **graph** **(DAG)** with $n$ [[Nodes|nodes]], find a **total ordering** of the nodes $x_1,\dots,x_n$, such that for any $i,j\leq n$, if $j>i$ then there is no path from $x_j$ to $x_i$ in $G$.
* A **total ordering** that satisfies this is called a **topological sort (TS)** of $G$.
* In the case of the example **graph**, a **TS** could be `1,6,3,2,4,7,5` or `6,1,2,7,3,4,5`.

Given a **DAG** $G$, let $x\leq y$ iff there is a path from $x$ to $y$.
$\leq$ is a **partial ordering**, since it can be trivially shown to be **reflexive**, **transitive**, and **antisymmetric**.

Conversely, if $(X,\leq)$ is a **partial ordering**, then let $G$ be the directed **graph** with **nodes** $X$ and  [[Arcs|arcs]] $\{(x,y):x\leq y \land x\neq y\}$.
* Here, $G$ is **acyclic**.

We could say that a **topological sorting** of a **DAG** amounts to a **linearisation** of a **partial ordering**, i.e. a **linear/total order** which extends the **partial ordering**.


We can perform **topological sorting** using [[Depth-First Search (DFS)|DFS]].
* The idea is that when we have finished processing a **node** $x$ (when we return to it after backtracking), we must have finished with all nodes which are reachable from $x$, and which come after $x$ in the sorting.
* So we can add a **node** to the sorted list (starting from the top) once we finish processing it.

For example, using the same **graph** as before:
* ![[Pasted image 20260128170456.png|300]]
	* We visit the **nodes** in the order `1,2,5,7,3,4,6`, assuming that the [[Adjacency Lists|adjacency lists]] are given in numerical order.
	* We exit the nodes in the order `5,7,2,1,4,3,6`.
	* So we obtain the sort `6,3,4,1,2,7,5`.

Here's the **python-like pseudocode**.
Note that:
* If we encounter a **cycle**, an **exception** is thrown.
* `ts` is initialised as an **empty array** of length $n$.
```Python
def dfsts(x):
	entered[x] = True
	for y in adj[x]:
		if entered[y]:
			if not excited[y]:
				raise Exception("Cycle")
		else:
			parent[y] = x
			dfsts(y)
	exited[x] = true
	tst[index] = x
	index = index-1

index = n-1
for x in nodes(G):
	if not entered[x]:
		dfsts(x)
```