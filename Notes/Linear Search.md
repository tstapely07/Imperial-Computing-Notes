---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
**Linear search** is one **algorithm** that solves the **unordered search problem**:
* Given an **unordered list** $L$ of elements of type $D$, denoted $L[0],\dots,L[n-1]$.
* Assume we have **random access** to any element $L[k]$.
* For a target element $x:D$:
	* If $x$ is in $L$, return index $k$ such that $L[k]=x$.
	* if $x$ is not in $L$ return "not found".

A **linear search** inspects $L[0],L[1],\dots,L[n-1]$ in turn, until the target $x$ is found, or the list ends.
* In the [[Worst Case vs Average Case Analysis|worst-case]], $W(n)=n$ comparisons.
* **Linear search** is [[Algorithm Analysis#^6b066c|optimal]] for **unordered lists**.

We can prove that **linear search** is **optimal**:
* Take any algorithm $A$ that solves the **unordered search problem**.
* We claim that if $A$ returns "not found", then it must have inspected every entry of $L$.
	* Now suppose that $A$ returns "not found" without inspecting an element at index $k$.  
	* If we change the input list $L$ so that $L[k]=x$, $A$ would still return "not found", since it skipped $k$.
	* This is **incorrect**, so we have a **contradiction**.
	* Hence in the worst case, $n$ comparisons are needed.
* $n$ is therefore our **lower bound**, and so **linear search** is indeed **optimal**.

For **ordered lists**, we can use **modified linear search**.
* This inspects the elements in order, but terminates early if it encounters an element $k$ that is strictly greater than $x$.
* This is safe, since $x$ could not appear after $k$.
* In the **worst case** this algorithm is still $W(n)=n$, since $x$ could be larger than all elements.
* In the **average case**, $A(n)\lt n$, due to the early termination in some cases.
* Here is the **decision tree** for $n=4$:
	* ![[Pasted image 20260303105346.png|257]]
	* $W(4)=4$ can clearly be extracted by looking at the **depth** of the **tree**.
* The **modified linear search** is not **optimal**. 
	* An **optimal** solution to the **ordered search problem** is the [[Binary Search|binary search]].