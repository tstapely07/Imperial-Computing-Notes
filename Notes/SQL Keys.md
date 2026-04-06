---
date: 2026-04-06
tags:
  - first-year
  - M40007
---

> [!Abstract] Definition
> The **candidate keys** are the possible valid [[Relational Keys|keys]] for a table.

> [!Abstract] Definition
> The **primary key** should be chosen as the key most often used to access the table.
> * The **primary key** has no logical impact.
> * An **index** is created on the **primary key**, allowing data to be accessed faster.

> [!Abstract] Definition
> All **candidate keys** not chosen as the **primary key** are known as **secondary keys**.

We can also declare [[foreign keys]] in **DDL**.

```SQL
CREATE TABLE account 
(
	no INTEGER NOT NULL
	type VARCHAR(8) NOT NULL
	cname VARCHAR(20) NOT NULL
	rate DECIMAL (4, 2) NULL
	sortcode INTEGER NOT NULL
	CONSTRAINT account_pk PRIMARY KEY (no)
	CONSTRAINT account_fk FOREIGN KEY (sortcode) 
	REFERENCES branch
)
```
Defines:
* ![[Pasted image 20260406093223.png|438]]
Note that the names `account_pk` and `account_fk` are only used to refer to the **keys** in **DDL**, such as `ALTER TABLE account DROP CONSTRAINT account_fk`.

We can define a **primary key** after a **table** has been created as follows:
```SQL
ALTER TABLE branch
ADD CONSTRAINT branch_pk PRIMARY KEY (sortcode);
```

We can also define **secondary keys** after a **table** has been created:
```SQL
CREATE UNIQUE INDEX branch_bname_key ON branch(bname);
```
* This ensures `bname` remains **unique**.
* It also improves lookup performance on `bname`.

