---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
The **edge-triggered D-type flip-flop** combines two [[The D-Type Latch|D-type latches]] (**primary** and **secondary**):
* ![[Pasted image 20260406143211.png|337]]
* This ensures that $Q$ reflects the state of $D$ at the exact instant that the [[Clocks|clock]] changes state from $1$ to $0$.
* The **primary latch** mirrors $D$ when the **clock** is $1$, at this stage the **secondary latch** is locked.
* The **secondary latch** only happens to mirror this data when the **clock** is $0$.
* And now, while the clock is $0$, the **primary latch** is locked.

We use this symbol, as shorthand for an **edge-triggered d-type flip-flop**:
* ![[Pasted image 20260406143750.png|145]]
Here is the full [[Sequential Circuits|sequential circuit]] for an **edge-triggered d-type flip-flop**:
* ![[Pasted image 20260406143437.png]]

We can represent an **edge-triggered d-type flip-flop** as a state machine, that only changes state on a falling edge of the **clock**:
* ![[Pasted image 20260406143817.png|288]]

Although the standard is a **falling edge-triggered d-type flip-flop**, there is also a **rising edge** variant, that triggers when the **clock** changes from $0$ to $1$:
* ![[Pasted image 20260406143919.png|307]]
* Constructing a **rising edge flip-flop** by negating the **clock** input to a **falling edge flip-flop** would cause the **clock** to be skewed, causing major problems.
* Instead, the **rising edge** variant requires a third **latch**.
	* When the **clock** changes from $0$ to $1$, this additional latch engages, sending a $0$ to the first **latch**, causing it to ignore $D$.

Other **edge-triggered flip-flops** than just the **D-type** also exist:
* The **T-type flip-flop** holds if $T=0$, and toggles if $T=1$:
	* ![[Pasted image 20260406145034.png|339]]
* The **J-K flip-flop** combines both the [[The R-S Flip-Flop|R-S flip-flop]] and the **toggle flip-flop**:
	* $J=0,K=1\to 0$
	* $J=1,K=0\to 1$
	* $J=K=0\to\text{ hold}$
	* $J=K=1\to \text{ toggle}$
	* ![[Pasted image 20260406145216.png]]
* We can also build a **rising-edge triggered flip-flop** with functionally to **preset** $Q=1$ or **clear** to $Q=0$:
	* ![[Pasted image 20260406145443.png|347]]
	* $\text{PRESET}=\text{CLEAR}=1$ causes the **circuit** to behave normally.