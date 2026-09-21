---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> The **closure** of some [[Attributes|attribute]] $X$, written $X'$, with some set of [[Functional Dependencies|FDs]] $S$ is the **set** of all **attributes** we can **infer** from $X$.

To compute $X'$, we can use the following **algorithm**, starting with $X'=X$.
* With $X'$, apply each **FD** $X_s\to Y$ in $S$ where $X_s\subseteq X^+$, but $Y$ is not already in $X^+$, to find new determined **attributes** $Y$.
* Now set $X^+=X^+\cup Y$
Repeat these steps until $Y$ is empty. 
* Once $Y$ is empty, we now have our **closure** $X^+$.

> [!Example]
> [[Relations|Relation]] $R(A,B,C,D,E,F)$ has **FD set** $S=\set{A\to BC,CD\to E, C\to F, E\to F}$
> To compute $A^+$:
> * Start with $A^+=A$.
> * Just $A\to BC$ matches, so $Y=BC$.
> * We now have $A^+ =ABC$, $C\to F$ matches, so $Y=F$.
> * Now $A^+ =ABCF$, no more **FDs** apply, so this is our result.
> 
> To compute $AD^+$.
> * Start with $AD^+=AD$.
> * Again, $A\to BC$ matches, so $Y=BC$.
> * Now $AD^+=ABCD$. $CD\to E$ and $C\to F$ match, so $Y=EF$.
> * Now $AD^+ = ABCDEF$, no more **FDs** apply, so we have our result. 
> 	* Note that since $AD^+$ is the entire set of **attributes**, $AD^+$ is a [[FDs and Keys|super-key]].
