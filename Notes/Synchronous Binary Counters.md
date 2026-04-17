---
date: 2026-04-06
tags:
  - first-year
  - M40001
---

One [[binary]] counter is a two **bit** counter, which has four states:
* $0$ ($00$)
* $1$ ($01$)
* $2$ ($10$)
* $3$ ($11$)
There are many orders to count in, but we will count $0\to1\to2\to3\to0\to\dots$.
* This means our counter is a **two-bit binary up counter**.

We first construct the [[State Transition Tables|transition table]] for our [[Synchronous Circuits|synchronous circuit]]:
* ![[Pasted image 20260406182204.png|252]]
We can then draw [[Karnaugh maps]]:
* ![[Pasted image 20260406182343.png]]
This gives our [[Boolean Algebra|Boolean equations]]:
* $D_1=Q_1'\cdot Q_2+Q_1\cdot Q_2'=Q_1\oplus Q_2$
* $D_2=Q_2'$
Now we have our final circuit:
* ![[Pasted image 20260406182512.png|301]]

As another example, this time with an input, we can construct a controlled three **bit** counter:
* ![[Pasted image 20260406182704.png|296]]
* When $C=0$, the counter counts up in even numbers:
	* $000\to010\to100\to110\to000\to\dots$
* When $C=1$, the counter counts down odd numbers:
	* $000\to111\to101\to011\to001\to000\to$
This gives the following **state transition diagram**:
* ![[Pasted image 20260406183016.png|312]]
We have some undefined transitions. 
* The safe way to handle these would be to reset the counter to $0$ for any undefined transition.
* To build a simpler circuit, we can treat these unknown states and transitions as "don't cares".
	* However, after doing this, we must check that the final circuit works correctly in all instances.
We get the following **transition table**:
* ![[Pasted image 20260406183210.png|305]]
We can then draw these **Karnaugh maps**:
* ![[Pasted image 20260406183237.png|338]]
* ![[Pasted image 20260406183314.png|339]]
* ![[Pasted image 20260406183332.png|336]]
This gives the following **Boolean expressions**:
* $D_1=C'\cdot Q_1'\cdot Q_2+C'\cdot Q_1\cdot Q_2'+C\cdot Q_3'+C\cdot Q_1\cdot Q_2$
* $D_2=Q_2'\cdot Q_3'+Q_1\cdot Q_2'$
* $D_3=C\cdot Q_2+C\cdot Q_3'+C\cdot Q_1$
Now, we copy out whether a "don't care" was a $1$ or a $0$ back to the **transition table**:
* ![[Pasted image 20260406183529.png|309]]
And we get the following **state diagrams**:
* ![[Pasted image 20260406183556.png|319]]
* ![[Pasted image 20260406183606.png|323]]
* Since, from every unused state, we eventually return to a valid state, and never get stuck in a state we shouldn't, all our "don't cares" are safe.
Now we know they are valid, we can simplify our **Boolean expressions**:
* $D_1=C'\cdot Q_1\oplus Q_2+C\cdot (Q_1\cdot Q_2+Q_3')$
* $D_2=Q_2'\cdot (Q_1+Q_3')$
* $D_3=C\cdot ((Q_1+Q_3')+Q_2)$
* Note that $(Q_1+Q_3')$ is repeated, but we only need to construct it once.
And finally, we have the **circuit**:
* ![[Pasted image 20260406184308.png|332]]