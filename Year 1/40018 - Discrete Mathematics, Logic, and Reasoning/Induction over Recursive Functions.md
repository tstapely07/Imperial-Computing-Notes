---
date: 2026-04-17
tags:
  - first-year
  - M40018
---
We've [[Structural Induction over Lists|seen]] that every **inductively defined** **set**, **relation**, or **function** gives rise to a **successor relation**, such as $+1$ for $\mathbb{N}$ or `Node` for **trees**.
* This **successor relation** means that every **inductively defined** **set**, **relation** or **function** inherently has an **inductive principle**.

Let's consider this **function**:
```Haskell
M :: Int -> Int
M m = M'(m, 0, 1)

M' :: (Int, Int, Int) -> Int
M' (i, cnt, acc)
	| i == cnt = acc
	| otherwise = M'(i, cnt+1, 2* acc)
```
Let's do an example **trace**:
$$\begin{align}
M(3)&=M'(3,0,1)\text{ -- by definition of } M\\
&=M'(3,1,2)\text{ -- by second case in definition of } M'\\
&=M'(3,2,4)\text{ -- by second case in definition of } M'\\
&=M'(3,3,8)\text{ -- by second case in definition of } M'\\
&=8\text{ -- by first case in definition of } M'\\
\end{align}$$
In general, we see $M(m)=2^m$
Now, what if we wanted to prove $\forall m: \mathbb{N}.M(m)=2^m$
Well to do this, we essentially must prove: 
$$\forall m, cnt, acc, p:\mathbb{N}.[M'(m,cnt,acc)=p\to p=2^{(m-cnt)}\cdot acc]$$
If we tried to prove this by [[Mathematical Induction|induction]] over $M$, we get this **induction principle**:
* ![[Pasted image 20260417201946.png|635]]
However in the **inductive step** we end up with something like this:
* ![[Pasted image 20260417202013.png|542]]
And now we are stuck, since $M'(k+1,cnt,acc)$ is not defined in terms of $M'(k, cnt, acc)$.
* We could reason over $m-cnt$ being **decreasing**, but this is **indirect**.

Let's consider this function:
```Haskell
F :: Int -> Int
F 0 = 0
F i = 1 + F (i-3)
```
We can represent the second rule as $\forall i, j :\mathbb{Z}.[i\neq 0 \land F\;(i-3)=j\implies F\;i=1+j]$
* This states that the value of $i-3$ is used to calculate the value of $F\;i$.
Now, given $F\;0=0$ and $\forall j,k:\mathbb{Z}.[j\neq 0\land F\;(j-3)=k\to F\;j=1+k]$,  and some predicate $Q\subseteq \mathbb{Z}\times\mathbb{Z}$, we obtain the following **inductive principle** to prove that $\forall j,k\in \mathbb{Z}.[F\;j=k\to Q(j,k)]$:
* ![[Pasted image 20260417205356.png|520]]
* Notice that we do not try and prove $\forall j:\mathbb{Z}.Q(j,F\;j)$, since $F$ is not guaranteed to terminate.
* Our antecedent $F\;j=k$ ensures we only consider cases when $F$ terminates.

Now we can return to the function $M$ from before:
```Haskell
M m = M'(m, 0, 1)
M' (i, cnt, acc)
	| i == cnt = acc
	| otherwise = M'(i, cnt+1, 2* acc)
```
We represent it with these three equations:
* $\forall i: \mathbb{N}.M(i)=M'(i,0,1)$
	* This is shorthand for $\forall i,k:\mathbb{N}.[M'(i,0,1)=k\land M(i)=k]$
* $\forall i, acc:\mathbb{N}.M'(i,i,acc)=acc$
* $\forall i,cnt,acc,k:\mathbb{N}.[i\neq cnt\land M'(i,cnt+1,2*acc)=k\rightarrow M'(i,cnt,acc)=k]$
From the second and third equations, we get our **inductive principle**:
* ![[Pasted image 20260417210403.png|464]]
And the proof that $\forall m.M(m)=2^m$ would** be something like this:
* ![[Pasted image 20260417210541.png|419]]
* Now we have the schema, the proofs themselves are easy.
Note this form of **induction** on the **definition** of a **function** cannot prove termination.
* This is because we actually assume **termination** when constructing our **inductive principle**.
* Instead, we must prove **termination** by considering the functions arguments, to prove some measure is **strictly decreasing**.
