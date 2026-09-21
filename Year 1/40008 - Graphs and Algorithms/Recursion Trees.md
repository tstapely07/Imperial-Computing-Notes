---
date: 2026-03-04
tags:
  - first-year
  - M40008
---
Many **algorithms** follow the [[Divide and Conquer Algorithms|divide and conquer]] paradigm, each with its own **recurrence relation**:
* Worst case comparisons for [[Binary Search]]: $W(n)=W(\frac{n}{2})+1$
* Worst case comparisons for [[Merge Sort]]: $W(n)=2W(\frac{n}{2})+(n-1)$
* Number of arithmetic operations for [[Strassen's algorithm]]: $A(n)=7A\left( \frac{n}{2} \right)+18(\frac{n}{2})^2$

In general, a **divide and conquer** algorithm:
* Does work $T(n)$ for an input size $n$.
* Splits into $a$ **sub-problems**, of size $n/b$.
* Does $f(n)$ non-recursive work splitting and combining.
The corresponding **recurrence relation** is:
$$T(n)=aT\left(\frac{n}{b}\right)+f(n)$$
* We aim to solve this up to [[Formal Definitions of Big-O and Big-Theta|Big-Theta]] ($\Theta$).

We can draw **recursion** [[Trees - Graphs|trees]] for our **recurrence relations**.
* For example, consider:
	* $T(1)=1$
	* $T(n)=aT(n/2)+n$
	* This is like our general case, but with $b=2$ and $f(n)=n$.
Our **recursion tree** will start with an input of size $n$.
* Each unfolding of the recursion takes us down one level, to $a$ subproblems each with the size halved.
* Each [[Nodes|node]] of the **tree** records the size and the non-recursive work done. 
For this case, here's the **recursion tree**:
* ![[Pasted image 20260304190024.png|442]]
If $n=2^k$ then the **total work done** is the sum of the work at each of the $k+1$ levels:
$$n+a\left( \frac{n}{2} \right)+a^2\left(\frac{n}{2^2}\right)+\dots+a^{k-1}\left(\frac{n}{2^{k-1}}\right)+a^k$$
$$=n+\left( \frac{a}{2} \right)n+\left( \frac{a}{2} \right)^2n+\dots+\left(\frac{a}{2}\right)^{k-1}n+a^k$$

This is a **geometric series**.
* Take any **geometric series** $a,ar,ar^2,\dots,ar^k$, where $r>=0$, $r\neq 1$, and $r$ does not depend on $n$. 
* Let $t(n)$ be the largest term in the **series**.
* The **sum** of the **series**, $\sum\limits_{i=0}^kar^i=\Theta(t(n))$.
We can apply this fact to our **geometric series** from the **recursion tree**:
* In our case, with $b=2$, the **common ratio** $r=\frac{a}{2}$.
	* The **largest term** depends on whether $r\leq 1$, $r=1$, or $r\gt 1$
	* So in our case, the **critical threshold** is when $\frac{a}{2}=1$, so when $a=2$.
* If $a\lt 2$ then the greatest term is $n$.
	* So $T(n)=\Theta(n)$.
	* Here, the **non-recursive work** at level $0$ dominates.
* If $a=2$ then $T(n)=(k+1)n$
	* Using the assumption that $n=2^k$, so $k=\log_2 n$, we can obtain $T(n)=n\log_2 n+n$.
	* So $T(n)=\Theta(n\log n)$.
	* Here, the work is roughly **evenly spread** at all levels.
* If $a>2$ then the greatest term is $a^k$.
	* Again, $n=2^k$, so $a^k=a^{\log n}=n^{\log a}$.
	* So $T(n)=\Theta(n^{\log a})$.
	* Here, the **base cases** dominate.


