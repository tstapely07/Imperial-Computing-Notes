---
date: 2026-04-07
tags:
  - first-year
  - M40008
---

> [!Abstract] Definition
> A **binary heap structure** is a **left-complete** binary [[Trees - Graphs|tree]].
> * **Left-complete** means that if the tree has [[Tree Depth|depth]] $d$: 
> 	* All [[nodes]] are present at [[Node Depth|depth]] $0,1,\dots,d-1$.
> 	* At depth $d$, no **node** is missing to the left of a **node** which is present.
> 	* For example:
> 		* ![[Pasted image 20260305110639.png|385]]
> 	* The **rightmost** **node** at **depth** $d$ is the **last** **node**. 
> 		* In this case, $2$.

> [!Abstract] Definition
> A **tree** $T$ is a **minimising partial order tree** if the key at any **node** $\le$ the keys at each **child node**.
> * A heap structure with this property is a **min heap**:
> 	*  ![[Pasted image 20260305110822.png|384]]

> [!Abstract] Definition
> A **tree** $T$ is a **maximising partial order tree** if the key at any **node** $\ge$  the keys at each **child node**.
> * A heap structure with this property is a **max heap**:
> 	* ![[Pasted image 20260305110928.png|390]]

> [!Note]
> For any **node** in a **heap**, the left and right **subtrees** below it are also **heaps**, of the same type.
> 

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
