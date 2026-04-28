---
date: 2026-04-17
tags:
  - first-year
  - M40018
---
As well as [[structural induction over lists]], we can define **structural induction principles** over any [[Haskell]] **data structure**.
Here are some examples:
* ![[Pasted image 20260417145907.png|502]]
* Note that for `data Tree a`, we could move the $\forall x:[T]$ to the right of the implication, to get $\forall x:T.P(Node\;t1\;x\;t2)$, but this is logically equivalent.

When we struggle with a proof, we have two solutions:
* One is to invent some **auxiliary Lemma**.
The second is to strengthen the property we are trying to prove.
* We do this by replacing some specific case, such as a $0$, with a **universal quantifier**.
* This makes the proof more general, and in many cases, easier.

Finally, note that we can also build an **inductive principle** for a **mutually recursive** **datatype**.
Here's an example of this:
* ![[Pasted image 20260417183648.png|478]]
* We would prove this by first proving two **base cases**, `P(BaseR)` and `Q(BaseG)` separately.
* For the **inductive step**, we can again prove each separately, making sure to only use the correct **inductive hypothesis**.

Here's another **inductive principle** for a **mutually recursive datatype**:
```Haskell
data Tree = Leaf | Node Trees
data Trees = Empty | Cons Tree Trees
```
* ![[Pasted image 20260417184035.png|513]]
	* Here, when proving for `Cons`, we would assume both `P(t)` and `Q(ts)`, in order to show `Q(Cons t ts)`.
	* For `Node` we only assume `Q(ts)`, and we must reach `P(Node ts)`.

We can define **principles** in ways that help us to, such as here:
* ![[Pasted image 20260417204322.png|509]]
* This likely ends up being easier than **induction** over $S_\mathbb{N}$, and checking $Even$.
