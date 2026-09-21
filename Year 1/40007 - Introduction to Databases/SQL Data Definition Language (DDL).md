---
date: 2026-04-06
tags:
  - first-year
  - M40007
---
**DDL** is used to define a [[relational schema]].

> [!Example] Examples
> ```SQL
> CREATE TABLE branch
> (
> 	sortcode INTEGER NOT NULL,
> 	bname VARCHAR(20) NOT NULL,
> 	cash DECIMAL (10, 2) NOT NULL
> )
> ```
> Defines:
> * ![[Pasted image 20260406092314.png|225]]
> ```SQL
> CREATE TABLE account 
> (
> 	no INTEGER NOT NULL,
> 	type VARCHAR(8) NOT NULL,
> 	cname VARCHAR(20) NOT NULL,
> 	rate DECIMAL(4, 2) NULL,
> 	sortcode INTEGER NOT NULL
> )
> ```
> Defines:
> * ![[Pasted image 20260406092330.png|385]]

There are many datatypes available in **SQL**:
* ![[Pasted image 20260406092515.png|597]]



