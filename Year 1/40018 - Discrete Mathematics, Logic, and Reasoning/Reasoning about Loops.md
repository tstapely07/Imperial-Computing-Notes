---
date: 2026-04-22
tags:
  - first-year
  - M40018
---
In **imperative languages** like [[Kotlin]], we have a number of loop constructs available to us:
* `while`
* `for`
* `repeat-until`/`do-while`

All of these loops can be expressed as a `while` loop, so we will just focus on reasoning about them.

Here's the general structure of a `while` loop:
* ![[Pasted image 20260422101000.png|439]]
* We have a **condition**, a loop **body**, and a [[Mid-Conditions|mid-condition]] $M$ that summarises the effect of the loop.

For a [[Function Specifications|function]] like this one:
* ![[Pasted image 20260422101239.png|361]]
* By looking at the code, we can construct **mid-conditions** for lines 7 and 14:
	* Line 7, by considering the effects of lines 5 and 6: $a[..)\approx a[..)_{pre}\land res=0\land i=0$.
	* Line 14, by working backwards from the post-condition: $a[..)\approx a[..)_{pre}\land res=\sum a[..)$.
* However the **mid-condition** on line 12 requires a little more thought.

We need to find a property $P$ such that:
* $\forall n\in \mathbb{N}.[P\text{ holds after }n\text{ iterations of the loop}]$
* If $P$ holds and the loop condition does not hold, then this implies the **mid-condition** $M$.
Then we know that if the loop terminates, then it will reach a state that satisfies $M$.
This property $P$ is called the **loop invariant**.

To show that $\forall n\in \mathbb{N}.[P\text{ holds after }n\text{ iterations of the loop}]$ we need to use [[mathematical induction]]:
$$[P(0)\;\land\;\forall k\in\mathbb{N}.[P(k)\longrightarrow P(k+1)]]\;\longrightarrow\;\forall n\in \mathbb{N}.P(n)$$
So we need to show:
* $P$ holds after $0$ iterations, i.e. immediately before the loop.
* If $P$ holds after $k$ iterations, then $P$ holds after $k+1$ iterations, i.e. if $P$ and `cond` hold and the loop `code` is run, then $P$ holds again.

For our `sum` example, we end up with this **invariant**:
* ![[Pasted image 20260422103128.png|482]]
* Note that the **mid-condition** is not usually included, but is left here to demonstrate when the **invariant** must be re-established.

Our **informal proof obligations** end up being:
* Prove that the code preceding the loop establishes the **invariant**, i.e. if $P$ holds and we run lines 5 and 6, then $I$ now holds.
	* ![[Pasted image 20260422103409.png|547]]
* Prove that the **invariant** is preserved by the loop body, i.e. if $I$ and $cond$ hold and we run lines 10 and 11, then $I$ still holds.
	* ![[Pasted image 20260422103419.png|437]]
* Prove that on termination of the loop the mid-condition holds, i.e. if $I$ and $\neg cond$ hold, then $M$ holds.
	* ![[Pasted image 20260422103431.png|304]]

Now we also need some way to track the **progress** of the loop.
We do this by finding some **integer expression** which:
* Is larger than some value at the end of each loop iteration.
* Decreases in **every** loop iteration.
We can then be sure the **loop** will **terminate**.
This **expression** is called the **loop variant**.

For our example of `sum`, with `while (i < a.size)`, we can use `a.size-i` as our **variant**, which is bounded below by $0$.

Here's a different **algorithm** to sum an [[Array Notation Conventions|array]]:
* ![[Pasted image 20260422111725.png|445]]
* This time we traverse from the **end** to the **beginning**, and so `i` is now a **suitable invariant**.

And here's a **function** that modifies the **input array** within the loop:
* ![[Pasted image 20260422111940.png|448]]

We have a [[Hoare logic]] **rule** for proving **partial correctness** of a `while` **loop**:
$$\frac{P \longrightarrow I \quad \{I \wedge \text{cond}\}\;\text{body} \;\{I\} \quad I \wedge \neg \text{cond} \longrightarrow Q}{\{P\}\quad \text{while(cond)} \,\{ \;\text{body} \;\} \quad\{Q\}}$$
So to prove **partial correctness**, we must show:
* The **loop invariant** $I$ holds before the loop is entered.
* Given the condition, the loop body re-establishes the **loop invariant** $I$.
* Termination of the loop and the **loop invariant** $I$ imply the **mid-condition** $M$ immediately after the loop.
To prove [[Partial vs Total Correctness|total correctness]] we must additionally prove:
* The **variant** $V$ is **bounded**: $\exists c\in \mathbb Z.\set{I\land\text{cond}}\;\text{body}\; \set{V\ge c}$.
* The **variant** $V$ decrease with each loop iteration: $\set{I\land\text{cond}}\;\text{body}\; \set{V_{old}\gt V}$.

Note to prove the [[Hoare Triples|Hoare triple]]:
$$\{I \wedge \text{cond}\}\;\text{body} \;\{I\}$$
We must show:
$$I[\overline{mod}\mapsto\overline{mod}_{old}\land \text{cond}[\overline{mod}\mapsto\overline{mod}_{old}]\land \text{body}\;\longrightarrow\; I$$
* Where $\overline{mod}$ is the list of **variables** modified in `body`.

Let's do a final example, with a full formal proof:
* ![[Pasted image 20260422113739.png|513]]
* Note that since `culSum` does not shadow the **array reference** $a$, we will not need to distinguish between $a$ and $a_{pre}$ or $a.size$ and $a.size_{pre}$.
* However, we will need to track the **contents** of $a$ carefully, hence the addition of $M_0$ to capture the initial unmodified contents of $a$.
We prove that the **invariant** holds before the loop is entered as follows:
* ![[Pasted image 20260422114301.png|468]]
* ![[Pasted image 20260422114311.png|470]]
We prove the **loop body** re-establishes the **invariant** like this:
* ![[Pasted image 20260422114331.png|470]]
* ![[Pasted image 20260422114409.png|470]]
* ![[Pasted image 20260422114356.png|473]]
And we prove the **mid-condition** holds after the loop like this:
* ![[Pasted image 20260422114441.png|467]]
* ![[Pasted image 20260422114451.png|463]]
* Note that, as expected, we did not need to refer to the code here.
Finally, we can prove that the loop **terminates** like this:
* Note that since the proof set-up is identical for each termination property, we can prove both at the same time.
* ![[Pasted image 20260422114825.png|447]]
* ![[Pasted image 20260422114839.png|449]]
* ![[Pasted image 20260422114858.png|449]]
Finally, as [[Function Calls with Returns|usual]], we prove that the [[Pre-Conditions and Post-Conditions|post-condition]] is established like this:
* ![[Pasted image 20260422115015.png|448]]

Note that if there is a `break`, we must prove that this establishes the **mid-condition** after the loop.
If we have a `continue`, we must prove that the **loop invariant** has been re-established.