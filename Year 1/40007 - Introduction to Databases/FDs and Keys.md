---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
[[Functional dependencies]] give us a formal way to define [[relational keys]].

> [!Abstract] Definition
> If a set of [[attributes]] $X$ in [[Relations|relation]] $R$ **functionally determines** all the other **attributes** of $R$, then $X$ is a **super-key** of $R$.

> [!Abstract] Definition
> If $X$ is a **super-key**, and it is not possible to remove any **attribute** from $X$ to form $X'$ and have $X'$ functionally determine all **attributes**, then $X$ is a **minimal key** of $R$.

> [!Example]
> Suppose $branch(sortcode,bname,cash)$ has the **FD set**:
> $$\set{sortccode\to bname,bname\to sortcode,bname \to cash}$$
> Clearly $\set{sortcode,bname}$ is a **super-key** since $\set{sortcode,bname}\to cash$.
> However, we have $sortcode\to \set{bname, cash}$ and $bname\to \set{sortcode,cash}$, so the **minimal keys** are $sortcode$ and $bname$.
