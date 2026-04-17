---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
A **dirty read anomaly** occurs when a [[Transactions|transaction]] reads **data** that was written by another **transaction** that has not yet **committed**.
* $T_1$ writes $x$. $T_2$ then reads $x$ before $T_1$ **commits**.
* Now, if $T_1$ **aborts**, then $T_2$ would need to **abort** too.
	* If $T_2$ has already **committed** and so cannot **abort**, then we are left with **data corruption**.

[[Serialisability and Recoverability|Recoverable histories]] do not **all** prevent **dirty reads**, they only ensure that $T_2$ doesn't **commit** before $T_1$ does.
* Note that we do know that $\neg RC\to DR$ and $\neg DR\to RC$.
> [!Example] Examples
> Here's a **dirty read** that is **unrecoverable**:
> * ![[Pasted image 20260414104504.png|466]]
> 
> But here, by moving $c_1$, we have a **dirty read** that is still **recoverable**:
> * ![[Pasted image 20260414104523.png|476]]