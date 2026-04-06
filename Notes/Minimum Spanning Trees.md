---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
We know that every [[Connectedness|connected]] [[Graphs|graph]] has a [[Spanning Trees|spanning tree]].
When dealing with [[Weighted Graphs|weighted graphs]] we want to find a **minimum spanning tree**:
* This is a **spanning tree** where the **sum** of the **weights** of its [[Arcs|arcs]] is as small as possible.

For example:
* Here is a graph, and a **spanning** tree of **weight** $12$:
	* ![[Pasted image 20260204131333.png|300]]
* But are two **minimum spanning trees**, each with weight $9$:
	* ![[Pasted image 20260204131425.png|300]]
	* Note that this shows **MSTs** need not be unique.

Let $G$ be a **weighted graph**.
The **weight** of a **spanning tree** $T$ for $G$ is the **sum** of the **weights** of the **arcs** of $T$.
$T$ is a **minimum spanning tree (MST)** for $G$ if:
* $T$ is a **spanning tree** for $G$.
* No other **spanning tree** for $G$ has smaller **weight**.