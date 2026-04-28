---
date: 2026-04-17
tags:
  - first-year
  - M40018
---
Let's consider these two [[Haskell]] **functions**:
```Haskell
elem :: Eq a => a -> [a] -> Bool
elem x [] = False
elem x (y:ys) = x == y || elem x ys
```
```Haskell
subList :: Eq a => [a] -> [a] -> [a]
subList [] ys = []
subList (x:xs) ys 
	| elem x ys = subList xs ys
	| otherwise = x:(subList xs ys)
```
Suppose we want to prove $\forall xs:[a].Q(xs)$, where $Q$ is defined as:
$$Q(xs)\triangleq \forall ys:[a].\forall z : a.[z\in ys\to z \notin subList\;xs\;ys]$$
*  Where $z\in ys$ is shorthand for $elem\;z\;ys$ and $z\notin ys$ is shorthand for $\neg(elem\;z\;ys)$.

We could define $P(n)$ as:
$$\begin{align}P(n)&\triangleq \forall xs: [a].\forall ys:[a].\forall z:[a].\\
&[length\;xs=n\to (z\in ys\to z\notin subList\;xs\;ys)]\end{align}$$
We have $\forall n:\mathbb{N}.P(n)\leftrightarrow \forall xs:[a].Q(xs)$.
* So we could prove $\forall n:\mathbb{N}.P(n)$, and achieve our desired goal.
We would end up with this [[mathematical induction]] **principle**:
* ![[Pasted image 20260417143726.png|530]]
The proof is doable, but the reasoning is **indirect**, and requires **lemmas**.

**Structural induction** gives us a better way.
The **structural induction principle** over [[lists]], for any type $T$, with $P\subseteq [T]$ is:
$$P([])\;\land\;\forall vs:[T].\forall v:T.[P(vs)\to P(v:vs)]\quad\longrightarrow\quad \forall xs:[T].P(xs)$$

> [!Example]
> Applying this to **principle** to $xs$ in our `subList` property gives us:
> * ![[Pasted image 20260417144112.png|474]]
> And the proof is as follows:
> * ![[Pasted image 20260417144223.png|474]]
> * ![[Pasted image 20260417144237.png|478]]
> * ![[Pasted image 20260417144304.png|481]]
> This is a much more natural proof structure than reasoning over length.

Note that, since we can freely swap **universal quantifiers**, we could also apply the **structural induction principle** to $ys$, giving this **principle**:
* ![[Pasted image 20260417144419.png|470]]

> [!Example]
> As another example, consider this **Haskell function**:
> ```Haskell
> rev :: [a] -> [a]
> rev [] = []
> rev (x:xs) = rev xs ++ [x]
> ```
> Let's prove that it satisfies:
> $$\forall xs:[a].\forall ys:[a].rev(xs\!+\!+ys)=(rev\;ys)\!+\!+(rev\;xs)$$
> Applying the **list induction principle** yields:
> * ![[Pasted image 20260417145011.png|502]]
> Let use define some **lemmas** that will be useful, for arbitrary $u:a,\;us,vs,ws:[a]$:
> * ![[Pasted image 20260417145115.png|467]]
> The proof is then as follows:
> * ![[Pasted image 20260417145150.png|466]]
> * ![[Pasted image 20260417145209.png|468]]

