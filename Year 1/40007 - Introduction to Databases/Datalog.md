---
date: 2026-04-10
tags:
  - first-year
  - M40007
---
In **Datalog**, everything is a **predicate**.
**Extensional predicates** are the data itself :
* ![[Pasted image 20260410105412.png|318]]
**Intentional predicates** define logical rules:
* ![[Pasted image 20260410105608.png|353]]
* They are written `Head :- Body`, which means `Head` depends on `Body`, and so `if Body then Head`.
* `Head` must be a single predicate, whereas `Body` can be any number of predicates

There are some rules for defining **predicates** and **variables**:
* The same name cannot be used for **intentional** and **extensional** **predicates**.
* **Predicate** names should begin with a lowercase letter.
* **Variables** should begin with a capital letter.
* A **variable** that only appears once, meaning its value is not significant, can be replaced by an `_`.