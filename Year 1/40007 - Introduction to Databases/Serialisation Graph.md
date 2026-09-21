---
date: 2026-04-14
tags:
  - first-year
  - M40007
---
Instead of swapping **operations** by hand to show a [[Transactions|transaction history]] is [[conflict serialisable]], we can use a **serialisation graph**.

To construct the [[Directed Graphs|graph]], we first a [[Nodes|node]] for every **transaction**.
* Every [[Conflicts|conflict]] is an [[Arcs|arc]], from the first **transaction** to the second.
* If the **graph** has no [[cycles]], then the **history** is **conflict serialisable**.
	* If there is a **cycle**, then the **history** is not **conflict serialisable**, although it could still be [[Serialisability and Recoverability|serialisable]], for example if some **transaction** blindly **overwrote** the **data item** that caused the **cycle**.
	
	