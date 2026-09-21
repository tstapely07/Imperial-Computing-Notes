---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
Here's a [[Function Specifications|function]] with **conditional branches**, annotated with [[Mid-Conditions|mid-conditions]]:
* ![[Pasted image 20260420204555.png|480]]
* On line $15$, we must be careful to write a **logical assertion** and not **code**, so something like $res=\max\set{res,z}$ would be **incorrect**.
* $res=\max\set{res_{old},z}$ would also be **incorrect**, since $res_{old}$ is never defined. This is an incorrect use of the $\__{old}$ [[Variables in Proofs|annotation]].

In general, for some code:
```Kotlin
// Pre: P
if (cond) {
	code1
} else {
	code2
}
//Post: Q
```
We have the following logical rule, using $P$ and the case of `cond` as assumptions to show $Q$ holds:
$$\frac{\set{P\land \text{cond}}\quad\text{code1}\quad\set Q\quad \set{P\land\neg\text{cond}}\quad\text{code2}\quad\set Q}{\set P\quad \text{if(cond)\{ code1 \} else \{ code2 \}}\quad \set Q}$$

We can introduce **mid-conditions** to make the proof structure more clear:
* ![[Pasted image 20260420205231.png|388]]
* We must have both $R_1\longrightarrow Q$ and $R_2\longrightarrow Q$.
Note that we may have $P\land \text{cond}\longrightarrow false$ or $P\land \neg\text{cond}\longrightarrow false$
* This simply means one branch is unreachable, and we can carry $false$ through the **mid-conditions**.
* $\set{false}\;\text{code}\;\set{false}$ always holds, and so obligation at the end of the branch becomes $false\longrightarrow Q$ which holds trivially.

Now if we go back to the first part of our `biggest` **function**, we can fill in **mid-conditions**:
* ![[Pasted image 20260420205525.png|339]]
This gives the following **informal proof obligations**:
* ![[Pasted image 20260420205546.png|394]]
* We could have used $M_1$ for both $R_1$ and $R_2$, to give us only these two **proof obligations**:
	* ![[Pasted image 20260420210127.png|425]]
	* But in general, the branches may not be so similar.
	* Often, the mid-condition after the **conditional branch** ends up being a **disjunction** of the effects of each **branch**.

Similarly we can add **mid-conditions** to the second part:
* ![[Pasted image 20260420205738.png|452]]
* Note that we do not need a **mid-condition** for the non-existent `else` branch.
We end up with the following **proof obligations**:
* ![[Pasted image 20260420205808.png|470]]
* Note that even though we did not have a **mid-condition** for the `else` branch, we still have a **proof obligation for it**, the final one.
