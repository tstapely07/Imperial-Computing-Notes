---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
When analysing a problem $P$, like [[Linear Search|sorting a list]], or finding a [[Shortest Path Problem|shortest path]], let $S$ be the set of all possible algorithms that solve $P$.
* Algorithms are typically ranked by how fast they run - their **time complexity**.

To determine if we have found the best possible algorithm, we must reason about **all** possible members of $S$, not just ones we know.
* A **lower bound** is a minimum amount of work which every member of $S$ **must do**.
	* For example, to search an **unsorted list**, we must inspect **every** element.
* If an algorithm's **time complexity** matches the problem's **lower bound**, the algorithm is considered **optimal**. ^6b066c
* Finding an **optimal** algorithm means there is no need to waste time looking for a faster one.



