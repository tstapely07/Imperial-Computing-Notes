---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
Here's a [[Sequential Circuits|sequential circuit]]:
* ![[Pasted image 20260406140651.png|242]]
We can construct its [[State Transition Tables|state transition table]], in the order `S R P Q`:
* ![[Pasted image 20260406140933.png|282]]
* Note that blue rows represent stable states.
We can construct its **transition diagram**:
* ![[Pasted image 20260406141021.png|344]]
This can be summarised as follows:
* ![[Pasted image 20260406141159.png|238]]
* Clearly, for input $11$, the output depends on the previous state.
Looking more in depth at input $11$ we see the following:
* ![[Pasted image 20260406141401.png|394]]
* Note that while it appears the two **unstable** states will oscillate indefinitely, in practice, it is likely to fall into some stable **state**, due to time delays. 

The **R-S Flip-Flop** acts as a single [[Binary|bit]] of **memory**, $Q$.
* Now observe that input $S$ is **set**, and $R$ is **reset**.
* We avoid using $S=R=0$, and so in all cases, $P=Q'$.
* The input $S=1,R=0$ will set $Q=1$.
* The input $S=0,R=1$ will set $Q=0$.
* The input $S=R=1$ ensure the output cannot change.
	* Since $P=Q'$, the **flip-flop** remains **stable**

 