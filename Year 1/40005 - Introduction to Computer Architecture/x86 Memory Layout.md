---
date: 2026-04-19
tags:
  - first-year
  - M40005
---
In [[x86]], **memory** is organised like this:
* ![[Pasted image 20260419102347.png|400]]
* The **stack** is managed automatically by the **compiler**, and is used for **local variables** and **function contexts**.
* The **heap** is managed by the **programmer**, and used for variables allocated using `new` or `malloc`.
* **Uninitialised/initialised data** is where **global** and **static** **variables** are stored.