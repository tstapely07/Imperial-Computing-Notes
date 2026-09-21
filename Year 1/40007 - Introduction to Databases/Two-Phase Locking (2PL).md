---
date:
tags:
  - first-year
  - M40007
---
While we've seen how [[serialisability and recoverability]] can confirm a [[Transactions|transaction history]] to be safe, a **DBMS** cannot confirm the safety of a **transaction** before it has occurred.
* To enforce safety in real-time, the **DBMS** uses **two-phase locking**.

There are two types of **locks**:
* **Read locks**, $rl_i[o]$, and **write locks**, $wl_i[o]$.
* A lock must be **locked** before the relevant **operation** is carried out, and **unlocked** afterwards, so we have the forms:
	* $rl_i[o]\dots r[o]\dots ru_i[o]$
	* $wl_i[o]\dots w[o]\dots wu_i[o]$
* A request for a **read lock** $rl_i[o]$ is only **refused** if $wl_j[o]$ is already held.
* A request for a **write lock** $wl_i[o]$ is **refused** if **any lock** $rl_j[o]$ or $wl_j[o]$ is already held.

Each **transaction** has two **phases**:
* In the **growing phase**, a **transaction** acquires **locks**, but may not release any.
* In the **shrinking phase**, a **transaction** releases **locks**, but is not allowed to acquire any new **locks**.
If, in the **growing phrase**, a **lock request** is refused, then the **transaction** is **delayed** for some amount of time.

In these **transactions**, $w_1[b_{34}]$ is a [[lost update]]:
* ![[Pasted image 20260414123143.png|415]]
In **2PL**, **locks** would have been requested like this:
* ![[Pasted image 20260414123217.png|479]]
* However $wl_2[b_{34}]$ would not have been granted, since $wl_1[b_{34}]$ is already held.
$T_2$ would have been **delayed**, perhaps leaving us with a **history** like this:
* ![[Pasted image 20260414123315.png|527]]

Any **history** from **2PL** is guaranteed to be [[conflict serialisable]], and therefore **serialisable**.
**2PL** does not guarantee **recoverability**. 
* A version known as **strict 2PL** does, by only allowing **write locks** to be released after the **transaction** has **committed** or **aborted**.

Looking at this graph we see that any [[Conflicts|conflicting]] **transactions** are forced to be staggered, since they both cannot hold all their **locks** simultaneously.
* ![[Pasted image 20260414123713.png|369]]
* We can therefore re-time all **operations** for each **transaction** to be within their respective peaks.
* This is clearly equivalent to a [[serial execution]], and so the **history** is indeed **conflict serialisable**.