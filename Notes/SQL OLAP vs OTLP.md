---
date: 2026-04-08
tags:
  - first-year
  - M40007
---
**Databases** handling [[SQL Data Manipulation Language (DML)|DML]] queries have two distinct types of workloads:
* **OLTP** (**Online Transactional Processing**) refers to the standard data processing, and only reads or writes to a few **rows** at a time.
	* For example, viewing and updating a single record.
* **OLAP** (**Online Analytical Processing**) refers to complex queries used for analysis. These queries read from many **rows**.
	* For example, summing an [[Attributes|attribute]] across an entire **table**.

> [!Note]
> In the real world, **OTLP** and **OLAP** are often separated into two physically separate databases, to prevent running **OLAP** queries from consuming all the resources and preventing **OTLP** queries from running, which would crash the application for everyday users.