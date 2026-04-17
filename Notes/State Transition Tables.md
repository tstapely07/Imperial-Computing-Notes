---
date: 2026-04-06
tags:
  - first-year
  - M40001
---
Here is a confusing circuit:
* ![[Pasted image 20260406134008.png|459]]
* When $A=1$, this circuit breaks down, since $R=(R.1)'=R'$, which is a contradiction.

In fact, [[logic gates]] are not instant, and there is some time delay $t_d$ between the input changing and the output reacting.

> [!Abstract] Definition
> A **state transition table** is a special truth table that maps the state **now** ($t$), to the **next** state ($t+t_d$).

* If the values in the **next** column match the values in the **now** column, then the circuit has settled to a **stable** state.
* If the **next** values differ from the **now** values, then the circuit will transition to a new state in the next time step.  
	* This is an **unstable state**.

We can construct the following **transition table** for the original circuit:
 * ![[Pasted image 20260406134439.png|211]]
This gives us the following **transition diagram**:
*  ![[Pasted image 20260406134512.png|220]]
