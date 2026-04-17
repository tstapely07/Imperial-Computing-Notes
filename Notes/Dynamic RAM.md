---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
For larger **memory** sizes, [[static RAM]] built out of [[Edge-Triggered D-Type Flip-Flop|D-Q flip-flops]] is no longer practical, since it is too large.
* Instead, one **transistor** and one **capacitor** are used for each [[Binary|bit]].
	* A charged **capacitor** represents a $1$, whilst an uncharged **capacitor** represents a $0$.

This store is not permanent, and so the **capacitor charge** must be restored multiple times a second.
* This is why this type of [[Synchronous Circuits|circuit]] is called **dynamic RAM**.
* The **capacitors' charges** are refreshed when the computer is not accessing the **memory**, and fortunately has a very low overhead.