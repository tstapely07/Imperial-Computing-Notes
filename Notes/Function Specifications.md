---
date: 2026-04-20
tags:
  - first-year
  - M40018
---
**Function specifications** are given in terms of [[Pre-Conditions and Post-Conditions|pre-conditions]] and [[Pre-Conditions and Post-Conditions|post-conditions]]:
* ![[Pasted image 20260420201437.png|477]]
This **specification** states that:
* For all $v_1,\dots,v_n$.
* If $P[x_1\mapsto v_1,\dots, x_n\mapsto v_n]$ holds before a call `someFunc(v1,..., vn`.
* Then $Q[x_1\mapsto v_1,\dots, x_n\mapsto v_n]$ will hold upon return.

Note that we must write $P[x_1\mapsto v_1,\dots, x_n\mapsto v_n]$, since $v_1,\dots,v_n$ are the actual values, whereas $x_1,\dots,x_n$ are just program variables.
* We can write $\bar x$ to mean $x_1,\dots,x_n$.

We can use the annotation $\__{pre}$ to refer the initial value of an input variable on entry to a function.
* We will only use $\__{pre}$ when necessary. Primitive variables such as `int`, `bool` and `char` cannot be modified, so it is not necessary here.
* Since all specifications refer to the current program state, we should never use $\__{old}$ in our assertions.

When a **function** returns a value, then the **post-condition** will normally be of the form $r=\dots$
* When a **function** returns a **boolean value** then the **post-condition** will normally be of the form $r\longrightarrow\dots$ or $r\longleftrightarrow\dots$
If the function does not have a **return type** then the **post-condition** will not include $r$.

To prove a **function** satisfies its specification, we must show that if property $P$ holds before the execution of `code` then after the execution of `code` property $Q$ must hold:
$$\set P\quad \text{code}\quad \set Q$$
* If the function parameters are shadowed within the body, then we would need to make the substitution $[\bar x \mapsto \overline {x_{pre}}]$ to both $P$ and $Q$.

For example, here's a **function**:
* ![[Pasted image 20260420203143.png|357]]
* This does not **shadow** the input parameters $x$ or $y$, so we do not need $\__{pre}$ or $\__{old}$ annotations for these variables.
We end up with the following **informal proof obligations**:
* ![[Pasted image 20260420203357.png|405]]
Which turn into the following **full logical assertions**:
* ![[Pasted image 20260420203419.png|398]]
* Most of these are trivial to prove, with only the last one requiring a small amount of work to show that $(x+y)^2=x^2+2xy+y^2$.
* This is often the case, the hard part is finding the **proof obligations**, rather than the actual **proof**.
