---
date: 2026-04-07
tags:
  - first-year
  - M40008
---
In a **priority queue**, each item `x` has a priority `key[x]`, which is usually a natural number.
* Items are removed lowest key first.
**Priority queues** are often implemented using [[Binary Heaps|min binary heaps]].
* To do this, we have a $1$-indexed array `E`,and a `heapsize`  tracker.
The core operations include:
* `PQcreate()`
	* Creates an empty array `E` with `heapsize = 0`.
* `isEmpty(Q)`
	* Checks if `heapsize == 0`.
	* Takes $O(1)$ time.
* `insert(Q,x)`
	* Adds an element `x` to the `Q`.
* `getMin(Q)`
	* Returns the root of the min heap at `E[1]`
	* This takes $O(1)$ time.
* `deleteMin(Q)`
	* Removes the minimum element by overwriting the root with the last element (`E[1]=E[heapsize]`).
	* `heapsize` is then decremented, and `fiMinHeap(1,heapsize)` is called to restore the min **heap property**.
	* This takes $O(\log n)$ time.
* `decreaseKey(Q,x,newkey)`
	* Updates `key[x] = newkey`.

`insert(Q, x)` is implemented by adding an item to the end of the array, and letting it percolate up until the **min heap property** is restored.
Here is the **python-pseudocode implementation**:
```Python
def insert(Q, x):
	heapsize = heapsize + 1
	E[heapsize] = x
	percolateup(heapsize)
	
def percolateup(c):
	if c > 1 :
		parent = c//2
		if E[c].key < E[parent].key:
			swap(c, parent)
			perculateup(parent)
```
* This runs in time $O(\log n)$.
When initially constructing the queue, it may be faster to do so in one go, in $O(n)$ time, then to insert elements one by one, which would take $O(n\log n)$ time.

`decreaseKey(Q, x, newkey)` can be implemented by locating the index `c` where `x` is located, updating its key, and calling `perculateup(c)` to restore the **min heap property**.
* Looking up `x` in what is essentially an **unsorted array** can only be done by a [[Linear Search|linear search]], taking $O(n)$ time.
* To solve this, we give each element some identifier, `id`, and use an additional array, `xref` to track locations, where `xref[id]=k` means that the element with that `id` is at index `k`.
* Now we can find the element's index `c` in $O(1)$ time, making the whole operation $O(n)$ time.
* Note that the `swap` operation used inside `percolateup` and `fixMinHeap` must also update the `xref` array accordingly.
