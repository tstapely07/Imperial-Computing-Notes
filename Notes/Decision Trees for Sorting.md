---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
Any comparison-based sorting algorithm can be visualised as a **decision** [[Trees - Graphs|tree]].
* The **internal nodes** represent the comparisons being made.
	* The tree branches left or right depending on the result.
* The **leaf nodes** represent the final rearranged lists - the sorted permutations.
* The **depth** represents the number of comparisons made.
	* The [[Worst Case vs Average Case Analysis|worst case]] number of comparisons of an algorithm is exactly equal to the maximum depth of its **decision tree**.

To successfully sort any possible list of length $n$, the algorithm's **decision tree** must account for every single possible permutation of those $n$ items.
* A list of length $n$ has exactly $n!$ possible permutations.
* Therefore any valid sorting **decision tree** must have at least $n!$ **leaf nodes**.

We can use the properties of **decision trees** to mathematically prove the absolute **minimum** number of comparisons any sorting algorithm must make.

If a **binary tree** has a depth of $d$, it can have at most $2^d$ leaves.
* Because a sorting tree for $n$ items must have at least $n!$ leaves, we can set up the inequality $2^d\ge n!$.
* Taking the logarithm of both sides gives $d\ge log_2(n!)$.
* Since the depth must be a whole integer, we round up, to give us our final result:
$$W(n)=\lceil log_2(n!)\rceil$$

The **average** case is determined by the **total** [[Paths|path length]], the sum of the [[Tree Depth|depths]] of all **leaf nodes**, divided by the total number of leaves, $n!$.
* To minimise the total path length, a tree must be perfectly [[Balanced Trees|balanced]].
* Any **unbalanced tree** can be restructured into a **balanced tree** without increasing its **total path length**.
* Since the **average depth** must be **only slightly** than the **maximum depth** $d$, we can conclude that:
$$A(n)=\lfloor log_2(n!)\rfloor$$
* This is correct since, unless $n!$ is a power of 2, which is not the case for $n\neq 2$, the floor of a logarithm is exactly one integer lower than its ceiling.
> [!Note]
> Now we can notice that the theoretical **average case** ($\lfloor log_2(n!)\rfloor$) is almost identical to the **worst case** ($\lceil log_2(n!)\rceil$)
> 
