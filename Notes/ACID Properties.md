---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
To be reliable, a **DBMS** must guarantee four properties.

**Atomicity** - if a [[Transactions|transaction]] crashes halfway through, the **DBMS** must undo partial changes.
* A **transaction** must either be fully completed, or leave no trace.

**Consistency** - a transaction must transform the **database** from one valid state to another, without violating any rules.

**Isolation** - **transactions** executed simultaneously must not interfere with each other. 
* They should act the same as if they were ran alone.

**Durability** - once a **transaction** **commits**, the changes must be permanent and written to storage.
