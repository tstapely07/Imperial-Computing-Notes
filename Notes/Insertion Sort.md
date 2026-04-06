---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
**Insertion sort** builds a **sorted list** one element at a time.
* Assume the sublist $L[0..i-1]$ is already sorted.
* Take the next element, $L[i]$, and filter it downwards by successively swapping it with the element to its left until it finds the correct position.
* Once placed, the sorted portion is now $L[0..i]$.

For each element $i$, from $1$ to $n-1$, the number of comparisons depends on the initial order:
* In the best case, the element $L[i]$ is already greater than $L[i-1]$.
	* It takes exactly $1$ comparison and stays in place.
* In the worst case, the element $L[i]$ is smaller than everything before it, i.e. the list is in reverse order.
	* The element must be compared $i$ times.
To find the total [[Worst Case vs Average Case Analysis|worst case complexity]], we sum the maximum comparisons for all $n-1$ steps:
$$W(n)=\sum_{i=1}^{n-1}i=\frac{n(n-1)}{2}$$
Because the highest power is $n^2$, the **worst case complexity** of **insertion sort** is $\Theta(n^2)$.