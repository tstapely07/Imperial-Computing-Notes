---
date: 2026-03-05
tags:
  - first-year
  - M40008
---
**Heapsort** uses a [[Binary Heaps|binary heap]] and relies on two helper functions, `fixMaxHeap` and `buildMaxHeap`.
* `fixMaxHeap` takes a single root node that is out of place, and performs swaps until the sub-tree is a valid **heap**.
* `buildMaxHeap` is a [[Divide and Conquer Algorithms|divide and conquer]] algorithm that walks through an unsorted array, and uses `fixMaxHeap` to construct a **max heap**.
* The main **Heapsort** algorithm simply calls `buildMaxHeap` once, and then repeatedly extracts the largest item.
	* After each extraction, `fixMaxHeap` is called to restore the **max heap property**.

`fixMaxHeap` restores the **max heap property** for a **node**, assuming that its left and right subtrees are already valid **max heaps**.
* Because it traces a single path down the tree to the leaves, it takes at most $2d$ comparisons, where $d$ is **depth**.
	* This means it runs in $O(\log n)$ time.
* Here's the **one-indexed** **python-like pseudocode** implementation:

```Python
def fixMaxHeap(root, heapsize):
	left = 2 * root
	right = 2 * root + 1
	
	if left <= heapsize: # root is not a leaf
		if left == heapsize # no right subheap exists
			largerSubHeap = left
		elif E[left].key > E[right].key:
			largerSubHeap = left
		else:
			largerSubHeap = right
		
		if E[root.key] < E[largerSubHeap].key: 
			# if the child is bigger, then we swap
			swap(root, largerSubHeap)
			# this may have disrupted the max heap property of the subtree, so we have a recursive call
			fixMaxHeap(largerSubHeap, heapsize)
```


`buildMaxHeap` is a [[Divide and Conquer Algorithms|divide and conquer]] algorithm, that recursively builds max heaps from the left and right subtrees, then uses `fixMaxHeap` to correct the root.
* If we assume the **heap** is a **complete** **binary tree**, then $n=2^k-1$.
	* The recursive calls take $W(\frac{n-1}{2})$ comparisons each.
	* Fixing the root at the end takes at most $2\log n$ comparisons.
	* So the [[Worst Case vs Average Case Analysis|worst case]] number of comparisons is given by the **recurrence relation** $W(n)=2W(\frac{n-1}{2})+2\log n$.
	* Applying the [[The Master Theorem|Master Theorem]] with $a=2$, $b=2$, $f(n)=2\log n$, our critical exponent is $E=1$.
		* Because the **root work** $f(n)=2\log n$ is **polynomially smaller** than the **leaf work** $n^E=n^1=n$, the **leaves dominate**.
		* So the **total work** is determined by the leaves, meaning $W(n)=\Theta(n)$.
		* So the **heap** can be built in **linear time**.
* Here is the **one-indexed** **python-like pseudocode** implementation:
```Python
def buildMaxHeap(root, heapsize):
	left = 2 * root
	right = 2 * root + 1
	if left <= heapsize:
		# so left subtree exists
		# ie root is not a leaf
		buildMaxHeap(left, heapsize)
		if right <= heappsize:
			buildMaxHeap(right, heapsize)
		
		fixMaxHeap(root, heapsize)
		# now the left and right subtrees, if they exist, are perfect max heaps
```

**Heapsort** builds a **max heap** and repeatedly extracts the minimum element, shrinking the heap while filling the **sorted array** from right to left.
* Overall, **Heapsort** requires $O(n\log n)$ comparisons.
* Here's the **one-indexed python-like pseudocode** implementation:
```Python
def heapsort(E, n):
	heapsize = n
	buildMaxHeap(1, heapsize)
	
	while heapsize > 1:
		swap(1, heapsize) # swap elements at index 1 and index heapsize
		heapsize = heapsize-1
		fixMaxHeap(1, heapsize)
```
* This works by storing the **heap** in the left side of the array, and storing the sorted part of the list in the right side of the array.
	* Eventually, the **heap** size has shrunk to 0, and we are just left with the sorted list.