---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
**Relational algebra** queries consisting of both [[Primitive Operators|primitive]] and [[Derived Operators|derived]] **operators** can be simplified using **equivalences**.

Equivalences involving **Project**:
**Project** and **Project**:
* $\pi_\vec{X} \pi_\vec{Y} R\equiv \pi_\vec{X} R$ 
* Inner projects can be eliminated.
* Note to be [[Well Formed Relational Queries|well formed]],  $\vec{X}\subseteq\vec{Y}$
**Project** and **Select**:
* $\pi_\vec{X}\sigma_{P(\vec{Y})}R\equiv \sigma_{P(\vec{Y})}\pi_\vec{x} R$
* If $\vec{Y}\subseteq\vec{X}$ then a project of $\vec{X}$ can be moved inside a select of $\vec{Y}$.
**Project** and **Product**:
* $\pi_\vec{X}(R\times S)\equiv \pi_{\vec{X}\cap Attrs(R)}R\times \pi_{\vec{X}\cap Attrs(S)}S$
**Project** and **Union**:
* $\pi_\vec{X}(R\cup S)\equiv \pi_\vec{X}R\cup \pi_\vec{X}S$
**Project** and **Difference**:
* $\pi_\vec{X}(R- S)\supseteq  \pi_\vec{X}R- \pi_\vec{X}S$
* Note that this is **not equivalent**.
* **Tuples** that are different in $R$ and $S$ could collapse into the same **tuple** after **projecting**.

Equivalences involving **Select**:
**Select** and **Select**:
* $\sigma_{P_X(\vec{X})}\sigma_{P_Y(\vec{Y})}R\equiv \sigma_{P_X(\vec{X})\land P_Y(\vec{Y})}R$
**Select** and **Product**:
* $\sigma_{P(\vec{X})}(R\times S)\equiv \sigma_{P(\vec{X})} R\times S$
* If $\vec{X}\subseteq Attrs(R)$ than a **select** can be moved onto $R$
**Select** and **Union**:
* $\sigma_{P(\vec{X})}(R\cup S)\equiv \sigma_{P(\vec{X})}R\cup\sigma_{P(\vec{X})}S$
**Select** and **Difference**:
* $\sigma_{P(\vec{X})}(R-S)\equiv \sigma_{P(\vec{X})}R-S$
* The following also holds, but results in needless filtering of $S$ which is computationally costly:
	* $\sigma_{P(\vec{X})}(R-S)\equiv \sigma_{P(\vec{X})}R-\sigma_{P(\vec{X})}S$

Equivalences involving **binary operators**:
**Product** and **Union**:
* $R\times (S\cup T)\equiv (R\times S)\cup (R\times T)$
**Product** and **Difference**:
* $R\times (S-T)=(R\times S)-(R\times T)$
**Difference** and **Union**:
* $R-(S\cup T)\equiv (R-S)-T$
