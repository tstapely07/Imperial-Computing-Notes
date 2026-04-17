---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> When analysing a [[Transactions|transaction history]] for conflicts, we are only interested in the **transactions** that get **committed**. 
> * We ignore all **operations** belonging to a **transaction** that **aborted**.
> * This is known as the **committed projection**.

> [!Example]
> ![[Pasted image 20260414110940.png]]