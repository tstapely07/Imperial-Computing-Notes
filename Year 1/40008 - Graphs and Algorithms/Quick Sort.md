---
date: 2026-03-04
tags:
  - first-year
  - M40008
---
**Quicksort** is a **recursive** **sorting** algorithm that works by splitting a list around a chosen **pivot**.
* Here, we arbitrarily choose the **pivot** to be the first element of the list.
* The list is then reordered so that elements $\le$ the **pivot** are placed before it, and elements $\gt$ the **pivot** are placed after it.
* The portions of the list before and after the pivot are then sorted **recursively**.
Here is the **python-like pseudocode** for the main recursive function:
* `L` is the list to be sorted, with length $n$.
* The initial call would be `quicksort(0, n-1)`.
```Python
def quicksort(left, right):
	if left < right:
		s = split(left, right)
		# L[s] is now in the correct position
		quicksort(left, s - 1)
		quicksort(s + 1, right)
```

The **split** call, `split(left, right)` splits the sublist `L[left..right]` around the pivot `d=L[left]`.
* It returns the index `s` of **pivot**.
* It uses two **pointers**, `i` and `j`, stepping through the list and swapping elements.
* Applying `split` to a list of length $n$ requires exactly $n-1$ comparisons.
Here is the **python-like pseudocode** for `split`:
```Python
def split(left, right):
	# pre-condition: left < right
	d = L[left] # pivot is the first element of the sublist
	i = left + 1
	j = right
	
	# invariant:
	left < i <= j+1
	j <= right
	if left <= k < i then L[k] <= d
	if j < k <= right then L[k] > d
	
	while i <= j:
		if L[i] <= d:
			i = i+1
		else:
			L[i], L[j] = L[j], L[i]
			j = j-1
				
	# now i = j + 1
	L[left], L[j] = L[j], L[left] # put pivot in its final, sorted, position
	return j
```
* Essentially, the **invariant** states that anything between `left` and `i` is $\le$ the **pivot**, anything between `j` and `right` is $\gt$ the **pivot**, and anything between `i` and `j` is yet to be processed.
* The final swap takes the pivot from the start, and puts it right between the smaller and larger elements.

**Quicksort's** sublists can vary in length, depending on the split, with the [[Worst Case vs Average Case Analysis|worst case]] occurring when the split happens at one end.
* This leaves us with only one list, of length $n-1$, to sort next.
* This **worst case** occurs when the list is already sorted.
* In this case, we get the recurrence relation:
	* $W(1)=0$
	* $W(n)=n-1+W(n-1)$
* Solving this gives:
$$W(n)=(n-1)+(n-2)+\dots+2+1=\frac{n(n-1)}{2}$$
* In this **worst case**, **Quicksort** is no better than [[insertion sort]].

Fortunately, the split is unlikely to occur at one end.
* This means that, as an exception to the normal rule, the **average** number of comparisons $A(n)$ is of lower order than $W(n)$.
* With a split position $s$, the left sublist goes from index $0$ to $s-1$, meaning it has  $s$ elements, so sorting it takes $A(s)$ comparisons.
	* The right sublist goes from index $s$ to $n-1$, meaning it has $n-s-1$ elements, so sorting it takes $A(n-s-1)$ comparisons.
* If we assume each position is equally likely, we can find the **average** cost of the recursive call, and define a **recurrence relation**:
$$\begin{gather}A(0)=0\\A(1)=0\\
A(n)=n-1+\frac{1}{n}\sum_{s=0}^{n-1}(A(s)+A(n-s-1))\end{gather}$$
* In fact, the second sum is the same as the first sum, just counting backwards.
	* We also recall that $A(0)=A(1)=0$, so we can ignore these terms.
* These simplifications give:
$$A(n)=n-1+\frac{2}{n}\sum_{i=2}^{n-1}A(i)$$
* Using **proof by induction** and bounding the summation with the integral $\int x\ln x$, it can be proven that $A(n)\le2n\ln n$.
* Therefore, the **average case** complexity is of [[Orders of Complexity|order]] $\Theta(n\log n)$.

While $W(n)$ for [[Merge sort]] is almost as good as the average case, $A(n)$ for **Quicksort**, **Quicksort** still excels in practice:
* It has a major advantage of operating **in place**, and not requiring extra space.
* It is also often possible to increase the chance of a favourable split.