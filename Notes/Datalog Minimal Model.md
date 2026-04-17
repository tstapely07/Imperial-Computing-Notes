---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
In [[Datalog]], the **minimal model** is the minimum set of **predicates** that must be true, given any combination of values assigned to the variables.
* If a **predicate** that the rules define to be true is excluded, then the set of **predicates** is not a **model**.
* If an unproven **predicate** is included, then the set of **predicates** is a **model**, but not a **minimal model**. 

> [!Example]
> With these **predicates**:
> * ![[Pasted image 20260410110326.png|365]]
> This is not a **model**, since it doesn't include `deposit_account(119, 'Poulovassilis, A.' 5.50, 56)`:
> * ![[Pasted image 20260410110419.png|452]]
> This is not a **minimal model**, since we could remove `deposit_account(127, 'Poulovassilis, A.' 4.50, 56)`:
> * ![[Pasted image 20260410110459.png|429]]
> This is a **minimal model**:
> * ![[Pasted image 20260410110518.png|478]]
> Note that the **minimal model** should technically include the **extensional predicates** already defined, but we usually omit these for brevity.