---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
To maintain good [[x86 Memory Layout|memory]] [[performance]], [[x86]] uses **alignment rules**:
* Any **primitive object** of $K$ [[Binary|bytes]] must start at a **memory address** that is a multiple of $K$.
This means:
* `char` - $1$ **byte** - no restrictions.
* `short` - $2$ **bytes** - multiple of $2$.
* `int`, `float` - $4$ **bytes** - multiple of $4$.
* `long`, `double`, **pointers** - $8$ **bytes** - multiple of $8$.

To achieve this when defining [[x86 Structures|structures]], the **compiler** must insert empty space between **variables**, known as **padding**.
* The total size of the `struct` itself must be a perfect multiple of $K_{max}$, where $K_{max}$ is the largest alignment requirement of any individual element inside it, Also the starting address for the `struct` must be a multiple of $k_{max}$.
* [[x86 Arrays|Arrays]] must be aligned to the size of their individual elements.
Sometimes, the order we define **elements** can actually save us space:
* ![[Pasted image 20260420155449.png|491]]
* In general, we should define **elements** from **largest** to **smallest**.