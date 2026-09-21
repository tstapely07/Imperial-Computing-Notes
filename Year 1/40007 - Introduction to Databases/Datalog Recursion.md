---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
[[Datalog]] inherently supports recursion, which is achieved by using the name of a **predicate** within its own body.
* The **predicate** must also be defined for the base case.
Like in [[SQL Data Manipulation Language (DML)|SQL]] [[SQL Recursion|recursion]], the **recursion** terminates when no new results are found.

> [!Example]
> These **predicates**:
> * ![[Pasted image 20260410114211.png|230]]
> * ![[Pasted image 20260410114217.png|360]]
> Give the following [[Datalog Minimal Model|minimal model]]:
> * ![[Pasted image 20260410114407.png|221]]