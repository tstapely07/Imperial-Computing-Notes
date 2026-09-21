---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
A [[Serialisability and Recoverability|recoverable]] [[Transactions|transaction history]] prevents **data corruption**, since if a **transaction** **aborts**, then any other **transactions** depending on it can also be **aborted**.
* However, we can get cases where a chain of **transactions** depend on each other.
* **Aborting** the last one results in **cascading aborts**, which negatively impacts performance.

> [!Abstract] Definition
> A **history** **avoids cascading aborts** (**ACA**) if **transactions** are blocked from reading any **data** until the **transaction** that wrote it has **committed**.
> * This eliminates the [[dirty read]] **anomaly**.
> * Note that $ACA\subset RC$

This **transaction history** is **recoverable**, but not **ACA**.
* ![[Pasted image 20260414113920.png|411]]