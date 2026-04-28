---
date: 2026-04-21
tags:
  - first-year
  - M40018
---
Reasoning about **recursive functions** can be done using the same techniques as reasoning for general [[function calls]].
* We can assume the [[Function Specifications|function's specification]] holds when it is called in the function body.
* This allows us to make use of [[modular verification]].

Here, we use `sum` to set up a call to `sumAux`:
* ![[Pasted image 20260421164107.png|508]]
* ![[Pasted image 20260421164208.png|497]]
We can reason about `sum` with the following **informal proof obligations**:
* ![[Pasted image 20260421164229.png|480]]
* Here, we can assume the [[Partial vs Total Correctness|correctness]] of `sumAux`.
From the **proof obligations** we get the following **full logical assertions**:
* Line 5:
	* ![[Pasted image 20260421164316.png|204]]
* Line 6:
	* ![[Pasted image 20260421164421.png|453]]
	* In general we need to distinguish between $a[..)_{old}$ and $a[..)_{pre}$, but since no code has run before line 5, we know that $a[..)_{pre}$ passed to `sumAux` is the same as $a[..)_{pre}$ passed to `sum`.
* Line 7:
	* ![[Pasted image 20260421164608.png|385]]

Now let's reason about `sumAux`, defined like this:
* ![[Pasted image 20260421171808.png|539]]
* Note since $a$ and $i$ are not shadowed, we do not need to distinguish between $a$, $a_{pre}$ or $a_{old}$ or between $i$, $i_{pre}$ or $i_{old}$, although we do need to carefully track the contents of $a$.
We can represent the **recursion** graphically, like this:
* ![[Pasted image 20260421172036.png|457]]
Like any other **function call**, we get the following **informal proof obligations**:
* ![[Pasted image 20260421172111.png|541]]
We can then obtain these **formal logical assertions**:
* Line 6:
	* ![[Pasted image 20260421172338.png|479]]
	* This part of the [[Conditional Branches|conditional branch]] corresponds to the **base case**.
* Line 7:
	* ![[Pasted image 20260421172420.png]]
	* This proof relies on the property that $\forall k.\left[\sum[k..k)=0\right]$
* Line 9:
	* ![[Pasted image 20260421172526.png]]
	* This corresponds to the `else` **clause**, which is for the **inductive branch**.
* Line 10:
	* ![[Pasted image 20260421172606.png]]
* Line 11:
	* ![[Pasted image 20260421172627.png]]
	* Here, including $0\le i\ \lt a.size$ is crucial, to ensure that `a[i]` is valid.
	* Note that if the order of line 10 was swapped, to read `val res = sumAux(a, i+1) + a[i]`, we would now describe this as `res=r+a[i]`, no longer with an $\__{old}$ **annotation**. In this case, `sumAux` guarantees the array is unmodified, so there is no difference, but that is not always the case.
* Line 12:
	* ![[Pasted image 20260421173423.png]]

What if we defined a function `sillySum` like this:
* ![[Pasted image 20260421173526.png|603]]
* `sillySum` is clearly [[Partial vs Total Correctness|partially correct]], but it is not **totally correct**.

We need some **measure of progress** to be able to reason about **termination**.
* For `sumAux`, this is `(a.size-i)`, since this decreases on every **recursive call**.

To show that `sum` terminates, we would need to prove:
$$\forall a\in int[], i\in\mathbb{Z}.[0\le i\le a.size\;\longrightarrow\;sumAux(a,i)\text{ terminates}$$
We could do this through [[mathematical induction]] on $a.size -i$:
* ![[Pasted image 20260421173835.png|486]]
* ![[Pasted image 20260421173903.png|471]]
