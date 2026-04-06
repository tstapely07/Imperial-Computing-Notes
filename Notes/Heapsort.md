---
date: 2026-03-05
tags:
  - first-year
  - M40008
---
A **binary heap structure** is a **left-complete** binary [[Trees - Graphs|tree]].
* **Left-complete** means that if the tree has [[Tree Depth|depth]] $d$: 
	* All [[nodes]] are present at [[Node Depth|depth]] $0,1,\dots,d-1$.
	* At depth $d$, no **node** is missing to the left of a **node** which is present.
	* For example:
		* ![[Pasted image 20260305110639.png|385]]
	* The **rightmost** **node** at **depth** $d$ is the **last** **node**. 
		* In this case, $2$.
* A **tree** $T$ is a **minimising partial order tree** if the key at any **node** $\le$ the keys at each **child node**.
	* A heap structure with this property is a **min heap**:
		* ![[Pasted image 20260305110822.png|384]]
* A **tree** $T$ is a **maximising partial order tree** if the key at any **node** $\ge$  the keys at each **child node**.
	* A heap structure with this property is a **max heap**:
		* ![[Pasted image 20260305110928.png|390]]
* For any **node** in a **heap**, the left and right **subtrees** below it are also **heaps**, of the same type.

**Binary heaps** can be implemented entirely using arrays, without the need for pointers.
* We store the **heap** level by level.
	* Note that we start at index $1$, to make the simplify the arithmetic.
* We can find any **node** at index $i$'s relatives using simple multiplication and division:
	* $i$'s left child is at $2i$.
	* $i$'s right child is at $2i+1$.
	* $i's$ parent is at $\lfloor \frac{i}{2}\rfloor$.
* This array structure allows **Heapsort** to be carried out **in place**.
* Let's see how the **heap** from earlier would be represented:
	* ![[Pasted image 20260305112019.png|356]]
	* `[16, 12, 13, 9, 5, 6, 8, 0, 7, 1, 3, 4, 2]`


**Heapsort** relies on two helper functions, `fixMaxHeap` and `buildMaxHeap`.
* `fixMaxHeap` takes a single root node that is out of place, and performs swaps until the sub-tree is a valid **heap**.
* `buildMaxHeap` is a [[Divide and Conquer Algorithms|divide and conquer]] algorithm that walks through an unsorted array, and uses `fixMaxHeap` to construct a **max heap**.
* The main **Heapsort** algorithm simply calls `buildMaxHeap` once, and then repeatedly extracts the largest item.
	* After each extraction, `fixMaxHeap` is called to restore the **max heap**.

`fixMaxHeap` restores the **heap property** for a **node**, assuming that its left and right subtrees are already valid **max heaps**.
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