---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
**Merge sort** is a [[Divide and Conquer Algorithms|divide and conquer algorithm]] that sorts a list by breaking it into smaller halves, sorting them, and then merging them back together.

The process is as follows:
* **Divide** - divide the list roughly into two halves.
* **Solve** - sort each half separately using recursion.
* **Combine/merge** - merge the two sorted halves back into a single sorted list.

The **base case** is the singleton list:
* The recursion stops when a list is of size $1$.
* This list is already sorted by definition, so the algorithm performs 0 comparisons at this level.

The **implementation** goes as follows:
* Note that the initial call to sort a list $L$ of length $n$ is `mergeSort(L, 0, n-1)`.
```Python
def mergeSort(L, left, right):
	if left < right:
		mid = floor((left + right)/2)
		mergeSort(L, left, mid)
		mergeSort(L, mid+1, right)
		Merge(L, left, mid, right) 
```

The **merge** step is the primary source of computational work in **merge sort**.
* It combines two sorted sublists into one sorted list.
* The algorithm compares the current first, and therefore lowest, element of each sublist, and outputs the smaller of the two.
* This continues until one of the sublists is exhausted.
	* At this point, the remainder of the other sublist is transferred without the need for further comparisons.
* For a final merged list of size $n$, at most $n-1$ comparisons are needed in the [[Worst Case vs Average Case Analysis|worst case]].
	* This **worst case** occurs when only one element remains in the second list when the first is exhausted.

The **worst case** number of comparisons $W(n)$ is given by the recurrence relation:
* $W(1)=0$
* $W(n)=n-1+W\left( \left\lceil  \frac{n}{2} \right\rceil \right)+W(\lfloor \frac{n}{2}\rfloor)$
	* Note that the $(n-1)$ term represents the comparisons required in the **merge** step.

We can compare the [[Decision Trees for Sorting|lower bound]] $\lceil log(n!)\rceil$ with $W(n)$ for **merge sort**:
* ![[Pasted image 20260303145545.png|461]]
* We can see that **merge sort** matches the theoretical **lower bound** exactly for $n\le 4$  
* For $n \gt 4$, **merge sort** still remains very close to the **lower bound**.

We can use **calculus** to prove it remains [[Algorithm Analysis|optimal]] as $n$ grows.
If we assume $n=2^k$, we can simplify the recurrence relation to:
$$W(n)=n-1+2W\left(\frac{n}{2}\right)$$
By repeating expansion, we can obtain:
$$W(n)=n\log_2(n)-n+1$$
Now we can clearly see that **merge sort** has a [[Formal Definitions of Big-O and Big-Theta|time complexity]] of $\Theta(n\log n)$.

The **lower bound** can be rewritten as follows:
$$\begin{gather}
\log (n!)\\
=\log(n\times(n-1)\times\dots\times1)\\
=\log(n)+\log(n-1)+\dots+log(1)\\
=\sum_{i=1}^n \log(i)
\end{gather}$$
For large $n$, this is approximately equal to the arrow under the curve $y=\log(x)$:
$$W(n)=\sum_{i=1}^n \log(i)\approx \int_1^n \log x \,dx$$
And since $\log x = c\ln x$, we get:
$$\int_1^n\ln x\,dx=[xln(x)-x]_1^n=n\ln n-n+1$$

So $W(n)$ and $\lceil \log(n!)\rceil$ are of the same [[Orders of Complexity|order]], $n\log n$.


