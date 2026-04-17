---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
A **tri-state buffer** has a single **data input**, and a **control input**.
* When $C=0$ the **buffer** acts like a normal wire, and outputs $D$.
* When $C=1$, the output is neither $0$ or $1$, and the **buffer** is effectively disconnected from the **data line**.
![[Pasted image 20260412104054.png|172]]

We can now use multiple **data sources** on a **single line**:
* ![[Pasted image 20260412104136.png|221]]
* We must ensure that only a single **tri-state buffer** has $C=0$, which can again be achieved by a [[Decoders|decoder]].