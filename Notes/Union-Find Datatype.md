---
date: 2026-02-04
tags:
  - first-year
  - M40008
---
Each **set** has a **leader** element which is the representative; of that **set**:
* `find` - find the leader of the **equivalence class**.
* `union` - merge two **classes**.

Operations:
* sets = `UFcreate(n)` - creates a family of singleton sets $\{1\},\{2\},\dots,\{n\}$ with `find(sets,x) = x`.
* `x'` = `find(sets,x)` - finds the leader `x'` of `x` within sets.
* `union(sets,x,y)` - merge the sets led by `x` and `y`, and use one of `x` or `y` as the new leader - note that `x` and `y` must be the leaders of their sets.

In a **naive** implementation, we maintain an array `leader` of nodes.
* `leader[x]` stores the leader of the set to which node `x` belongs.
* Initially `leader[x] = x` for all nodes.

Find is now $O(1)$, but union is $O(n)$.
This means that with the $O(n)$ unions required for [[Kruskal's Algorithm|Kruskal's algorithm]], we ended up with $O(n^2)$.

Instead, each set is stored as a (non-binary) [[Trees - Graphs|tree]].
* The **root node** is the representative (leader) of the set.
* We merge two sets by appending one **tree** to the other, so that the **root** of one **tree** is the **child** of the **root** of the other **tree**.
To store the **tree** structure, for each node `x` we maintain `parent[x]`, where `parent[x] = x` if `x` is the **root** (the leader).
* Initially `parent[x] = x` for any node `x`.
* `union(sets,x,y)` just involves setting `parent[y] = x` - which is $O(1)$.
* However `find` involves following `parent[x]` up to the **root**.
* Time taken is bound by the [[Tree Depth|depth]] of the **tree**.
* With **naive** merging of the **trees** like above, this can be as bad as $O(n)$.

To reduce the depth, we can take the **weighted union**:
* Since we can append **trees** in either order, we should always append the tree of lower size to the one of greater size.
* This requires us to store the size of the tree and update this, which is easy to do.
Using **weighted union**, the depth of a tree of size $k$ is $\leq\lfloor log \;k\rfloor$, this can be proved by **induction** on $k$ - see the lecture notes.

Now, using the **weighted union**, each `find` takes $O(log\;n)$, and each `union` takes $O(1)$.

**Union-find** can be further improved using **path compression**. ^b009cd
When finding the root for a node `x`, if this is not `parent[x]` then make `parent[y] = root` for all `y` on the `path` from `x` to the root:
* ![[Pasted image 20260204164354.png|250]]
This results in extra work, but keeping the **depth** of the **nodes** lower makes future finds faster.
It combines well with **weighted union** on size, since size is unchanged by **path compression**.
The **algorithm** goes like:
```Python
def cfind(x):
	y = parent[x]
	if y == x:
		root = x
	else:
		root = cfind(y)
		if root != y: # this if performs the path exception
			parent[x] = root
	return root
```

