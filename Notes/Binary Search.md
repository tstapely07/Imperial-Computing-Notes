---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
For searching **ordered lists**, instead of a [[linear search]] we can use **binary search**.
Rather than checking elements one-by-one, **binary search** looks at the middle element of the list.
* If the target is **smaller**, it repeats the process on the left half.
* If the target is **larger**, it repeats the process on the right half.
* Of course, if the target matches, then the element has been found.
* Here is its decision tree for $n=8$:
	* ![[Pasted image 20260303105804.png|300]]

Its **implementation** is as follows:
```Python
def binSearch(L, x, left, right):
	if left > right:
		return "not found"

	mid = left + (right-left) // 2
	
	if L[mid] == x:
		return mid
	elif x < L[mid]:
		return binSearch(L, x, left, mid-1)
	else:
		return binSearch(L, x, mid+1, right)
```

Each step **halves** the list, so each half has a length $\le \lfloor n/2 \rfloor$.
The recurrence relation is:
* $W(1)=1$.
* $W(n)=1+W\left( \left\lfloor  \frac{n}{2}  \right\rfloor \right)$
We can solve this by repeated expansion:
$$\begin{gather}
W(n)=1+W\left( \left\lfloor \frac{n}{2} \right\rfloor \right)\\
W(n) = 1 + 1 + W\left( \left\lfloor  \frac{n}{4}  \right\rfloor \right) \\
W(n) = 1 + 1 + 1 + W\left( \left\lfloor  \frac{n}{8}  \right\rfloor \right)\\
\dots\\
W(n)=\underbrace{1+\dots+1}_{k\;1s}+W(1)\\
W(n)=k+W(1)\\
W(n)=k+1
\end{gather}$$
The number of $1$s, $k$, is the number of times $n$ is divisible by $2$:
* $k=\lfloor log_2n \rfloor$
So the final **worst case complexity** is:
$$W(n)=1+\lfloor log_2n \rfloor$$

We can prove that **binary search** is [[Algorithm Analysis#^6b066c|optimal]] by representing any possible search algorithm $A$ as a **decision tree**.
* The tree must have at least $n$ nodes, to differentiate between $n$ items.
* For comparison based searches, the tree will be binary.

Firstly, if a **binary tree** has depth $d$, then it has $\le 2^{d+1}-1$ [[nodes]].
* We can prove this by induction:
	* Base case:
		* $d=0$
		* $2^{0+1}-1=1$
		* A tree of depth $0$, has just $1$ node, the **root node**, so the base case holds.
	* Inductive step:
		* Take two children with depth $\le d$, and assume they have $\le 2^{d+1}-1$ **nodes**.
		* Now consider a new **tree**, of depth $d+1$.
		* Total number of nodes $\le 1+(2^{d+1}-1)+(2^{d+1}-1)=2^{(d+1)+1}-1$
	* Hence shown by **induction**.

So the tree for algorithm $A$ has $\ge n$ **nodes**.
* If the maximum depth is $d$ then $n\le 2^{d+1}-1$.
* The **worst case performance** of $A$ corresponds to traversing to the deepest **leaf**, which is $d+1$ comparisons, so lets solve for $d+1$.
* So we obtain $n+1\le 2^{d+1}$, or $2^{d+1}\ge n+1$.
* Now we can take $log_2$ on both sides, to obtain $d+1\ge log_2(n+1)$.
* Operations must be **integers**, so we round up: $d+1\ge \lceil log_2(n+1)\rceil$
* So **any** search algorithm will require at least $\lceil log_2(n+1)\rceil$ in the **worst case**.
In fact, $\lceil log_2(n+1)\rceil$ is exactly equal to $1+\lfloor log_2n \rfloor$.
* This can be easily shown:
	* Let $k=\lfloor log_2 n\rfloor$
	* Then $2^k\le n \lt 2^{k+1}$
		* For an **integer** $k$, this is equivalent to:
		* $2^k\leq n \leq 2^{k+1}-1$
	* So $2^k \lt n+1 \le 2^{k+1}$
	* Hence $k \lt log_2(n+1)\leq k+1$
	* Therefore $\lceil log_2(n+1)\rceil=k+1$.
	* And substituting our definition for $k$ gives us the desired result:
	* $\lceil log_2(n+1)\rceil=1+\lfloor log_2n \rfloor$
* So the **worst case performance** of **binary search** is exactly equal to the **lower bound** for an **ordered search algorithm**.
* So **binary search** is **optimal**.

