---
date: 2026-04-05
tags:
  - first-year
  - M40007
---
Since all **operators** take [[relations]] as both inputs and outputs, they can be **chained**.
* However, these could cause problems.

> [!Abstract] Definition
> To be **well formed**:
> * The output of a **nested operator** must contain the **attributes** required by an outer [[Primitive Operators|primitive]] $\pi$ or $\sigma$.
> * ***Relations** must be [[union compatible]] where necessary.

![[Pasted image 20260405113452.png]]
* $\sigma_{type='current'}\pi_{no}account$ is **not well formed**.
* $\pi_{no}account-\pi_{no,mid}movement$ is **not well formed**.
* $\pi_{no}\sigma_{type='current'}account$ is **
