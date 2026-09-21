---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
[[x86]] provides [[Instruction Format|instructions]] for **arithmetic** and **bitwise** operations, as this table details:
* ![[Pasted image 20260418114732.png|555]]
* ![[Pasted image 20260418114749.png|451]]
* The `l` variants are given, but these work for all other **data sizes**.

There are some **operations** that give $128$-[[Binary|bit]] outputs.
* In these cases, the top half of the output is stored in the `%rdx` [[x86 Registers|register]], and the bottom half in `%rax`.
* ![[Pasted image 20260418115035.png|624]]

> [!Example] Examples
> ![[Pasted image 20260418115456.png|539]]
> ![[Pasted image 20260418115510.png|537]]


