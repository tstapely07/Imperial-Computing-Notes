---
date: 2026-04-21
tags:
  - first-year
  - M40018
---
Here's a general **function call** in [[Kotlin]]:
* ![[Pasted image 20260421102551.png]]
* ![[Pasted image 20260421102753.png|479]]
To show that a **function call** satisfies the caller's specification, we must show that $P$ satisfies the **function's** [[Pre-Conditions and Post-Conditions|pre-condition]] and that the **function's post-condition** satisfies $Q$.
This gives the following rule: 
* ![[Pasted image 20260421103058.png|548]]
* The **substitutions** of $[\bar x \mapsto\bar v]$ in $R$ and $S$ ensure we replace the **variables** in the function's specification with the actual **values** used.
* The additional **substitutions** of $[\bar v[..)\mapsto \bar v[..)_{old}]$ in $P$ and $[\bar v[..)_{pre}\mapsto \bar v[..)_{old}]$ in $S$ account for the possibility of the **function** changing the **program** **state**, such as if the contents of an array are modified.
	* The **substitution** in $S$ is necessary since, $\__{pre}$ is meaningless to the **caller**, whereas $\__{old}$ indeed refers to the **state** before the **call**, as desired.

Here's an example of a **program** with a **function call**:
* ![[Pasted image 20260421104914.png|498]]
We get the following **informal proof obligations**:
* ![[Pasted image 20260421105009.png|498]]
* Note that we must add $a[..)\approx a[..)_{pre}$ as part of $P_2$, since at the start of the **function** is the only time we can obtain this for free.
We end up with the following **logical assertions**:
* Line 12:
	* ![[Pasted image 20260421105336.png]]
* Line 13:
	* ![[Pasted image 20260421105517.png]]
* Line 14:
	* ![[Pasted image 20260421105553.png|511]]
	* The proof relies on the property $a[..)\sim b[..)\land b[..)\approx c[..)\longrightarrow a[..)\sim c[..)$.
* Line 15:
	* ![[Pasted image 20260421105728.png|529]]
* Line 17:
	* ![[Pasted image 20260421105752.png]]

