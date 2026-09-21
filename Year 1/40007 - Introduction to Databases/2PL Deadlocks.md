---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
While [[Two-Phase Locking (2PL)|2PL]] is incredibly safe, it introduces the problem of **deadlocks**.
* If $T_1$ holds a **lock** on $x$ and needs $y$, and $T_2$ holds a **lock** on $y$ and needs $x$, they will wait for each other forever.

To handle this, the **DBMS** draws a **waits-for-[[Directed Graphs|graph]]** in the **background**. 
* A [[Nodes|node]] is drawn for each [[transactions|transaction]].
* If $T_1$ requests a **lock** held by $T_2$, we draw a directed [[Arcs|arrow]] $T_1\to T_2$.
If a [[Cycles|cycle]] is ever encountered, a **deadlock** has occurred.
* This is resolved by **aborting** one of the **transactions**.

> [!Example] Examples
> Here, $T_1$ can execute after $T_2$ has finished: 
> * ![[Pasted image 20260414124842.png|277]]
> Here, we have a **deadlock**, and one **transaction** must be **aborted**:
> * ![[Pasted image 20260414124918.png|291]]