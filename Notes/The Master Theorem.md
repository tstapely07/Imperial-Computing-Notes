---
date: 2026-03-04
tags:
  - first-year
  - M40008
---
Building on our work on [[Recursion Trees|recursion trees]] for $b=2$, we work towards the **general case** for a [[Divide and Conquer Algorithms|divide and conquer]] algorithm.
* The **recurrence relation** is: 
$$T(n)=aT\left(\frac{n}{b}\right)+f(n)$$
The **recursion tree** will have $1+\log_b n$ levels:
* ![[Pasted image 20260304192515.png|408]]
* At level $0$, the **work done** is $f(n)$.
* At level 1, the **work done** is $af\left( \frac{n}{b} \right)$
* At level 2, the **work done** is $a^2 f\left( \frac{n}{b^2} \right)$
* At level $\log_b n$, the **work done** is $\Theta(a^{\log_b n})$

We define the **critical exponent** $E=log_b a=\frac{\log a}{\log b}$.
The solutions to our **recurrence relation** $T(n)$ are as follows:
1. If $n^{E+\epsilon}=O(f(n))$ for some $\epsilon\gt 0$ then $T(n)=\Theta(f(n))$.
	* Here, work at the **root** dominates.
	* So the **total work** is just the **non-recursive work** done at that top level.
2. If $f(n)=\Theta(n^E)$ then $T(n)=\Theta(f(n)\log n)$.
	* Here, work is **evenly spread**.
	* So the **total work** is the **work done** at one level, $f(n)$, multiplied by the number of levels, $\log n$.
3. If $f(n)=O(n^{E-\epsilon})$ for some $\epsilon\gt 0$ then $T(n)=\Theta(n^E)$.
	* Here, work at the **leaves** dominates.
	* So the **total work** is determined by the number of leaves, $n^E$.
* Note that for **polynomials**, it is sufficient to compare the $E$ to the **exponent** of $f(n)$ to work out which case we are in.
	* However, the formal definition in terms of $\epsilon$ is required to catch cases where the **work** at the **leaves** and the **work** at the **root** differs, but by **less** than a **polynomial factor**, such as a **logarithmic factor**.
	* Here, the **Master Theorem** does not apply.w

We can now apply the **Master Theorem** to our previous **divide and conquer** algorithms.
* For [[Binary Search]]:
	* The [[Worst Case vs Average Case Analysis|worst case]] number of comparisons is given by the **recurrence relation**:
	$$W(n)=W\left(\frac{n}{2}\right)+1$$
	* Here, $a=1$, $b=2$, and $f(n)=\Theta(1)=\Theta(n^0)$.
	* $E=\log_2 1=0$.
	* Since $E=0$ matches the exponent of $f(n)$, this is case 2, so the work is **evenly spread**.
	* So $W(n)=\Theta(n^0\log n)=\Theta(\log n)$.
* For [[Merge Sort]]:
	* The **worst case** number of comparisons is given by the **recurrence relation**:
$$W(n)=2W\left(\frac{n}{2}\right)+(n-1)$$
	* Here, $a=2$, $b=2$, and $f(n)=\Theta(n)=\Theta(n^1)$.
	* $E=\log_2 2=1$.
	* Since $E=1$ matches the exponent of $f(n)$, we again have case 2, where the work is **evenly spread**.
	* So $W(n)=\Theta(n\log n)$.
* For [[Strassen's Algorithm]]:
	* The number of arithmetic operations is given by the **recurrence relation**:
$$A(n)=7A\left( \frac{n}{2} \right)+18\left(\frac{n}{2}\right)^2$$
	* Here, $a=7$, $b=2$, and $f(n)=\Theta(n^2)$.
	* $E=\log_2 7 \approx 2.807$.
	* Since $E\gt 2$, we have **case 3**, where the **leaves dominate**.
	* So $A(n)=\Theta(n^{\log_2 7})$.
	* Here, any improvement to $f(n)$ will not improve the [[Orders of Complexity|order]] of $A(n)$.
	
