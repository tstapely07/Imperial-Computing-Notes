---
date: 2026-04-21
tags:
  - first-year
  - M40018
---
To reason about a [[Function Calls|function call]] with a **return value** we must show that the [[Pre-Conditions and Post-Conditions|pre-condition]] $R[\bar x \mapsto \bar v]$ is established before the call, and then we may assume that the **post-condition** $S[\bar x \mapsto \bar v]$ will hold after the call, and also that $res=r$ after the call.

Here we have a **function call** with a **return**:
* ![[Pasted image 20260421155256.png|443]] 
* Note that the **function** shadows $x$, so we must [[Variables in Proofs|track]] the value of this **variable**.

We end up with the following **informal proof obligations**:
* ![[Pasted image 20260421155350.png|511]]
And these gives us the following **logical assertions**:
* Line 10:
	* ![[Pasted image 20260421160326.png|177]]
* Line 11:
	* ![[Pasted image 20260421160523.png|74]]
* Line 12:
	* ![[Pasted image 20260421160606.png|312]]
* Line 13:
	* ![[Pasted image 20260421160627.png|133]]
* Line 14:
	* ![[Pasted image 20260421160643.png|309]]
* Line 15:
	* ![[Pasted image 20260421160716.png|183]]
	* Note that this shows us why the substitution $[x\mapsto x_{pre}]$ on $Q$ is necessary. Otherwise we would end up having to show: $x=x_{pre}+1\land r=x\;\longrightarrow\; r=x$, which would hold trivially.
	* This substitution is only necessary since it is written in terms of the original input $x$, which was **shadowed**.
