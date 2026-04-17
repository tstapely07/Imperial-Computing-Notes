---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
In standard [[Datalog]] rules only define what is true.
* To filter data by what is not true, we use **negation**.
* This is the equivalent of [[SQL Set Operators|EXCEPT]] in [[SQL Data Manipulation Language (DML)|SQL]].

We **negate** a **predicate** using $\neg$.

> [!Warning]
> Every variable that appears in a **negated predicate** in the body of a rule must also feature in a **non-negated predicate**:
> * This is known as **safe negation**.
> * Otherwise, we would be asking for anything that does not satisfy the **predicate**, without any other bound, resulting in an infinite result set.

> [!#Example]
> ```Datalog
> dormant_account(No) :-
> 	account(No,_,_,_,_),
> 	¬movement(_,No,_,_).
> ```
> This gives the following [[Datalog Minimal Model|minimal model]]:
> * ![[Pasted image 20260410112204.png|349]]
> 