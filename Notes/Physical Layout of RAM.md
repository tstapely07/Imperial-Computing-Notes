---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
[[Static RAM]] is generally arranged in a **2D** **grid**.
* We have separate [[Decoders|decoders]] for the **row** and **columns**. 
* One **row decoder** will output a $1$ across the entire **row**, and one **column decoder** will output a $1$ across the entire **column**.
* This **row** and **column** will overlap on a single **cell**.
* ![[Pasted image 20260412110147.png|275]]

Each **cell** is connected to the same **read/write line** and **data line**.
* The **data line** is then connected to the main [[System Buses|data bus]] using a two-way [[Tri-State Buffers|tri-state buffer]].
* This lets us combine multiple **RAM** **chips** to build higher capacity **memory**.
* ![[Pasted image 20260412111730.png|311]]
