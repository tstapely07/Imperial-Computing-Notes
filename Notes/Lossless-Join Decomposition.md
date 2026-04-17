---
date: 2026-04-13
tags:
  - first-year
  - M40007
---
> [!Abstract] Definition
> A **loss-less join decomposition** of a [[Relations|relation]] $R$ with respect to [[Functional Dependencies|FDs]] $S$ into **relations** $R_1,\dots,R_n$ has the properties that:
> * $Attrs(R_1)\cup \dots \cup Attrs(R_n)=Attrs(R)$
> * For all possible **extents** of $R$ satisfying $S$, $\pi_{attrs R_1}R\bowtie\dots\bowtie \pi_{R_n}R=R$.

If a **decomposition** is not **lossless**, then some **tuples** spread over $R_1,\dots,R_n$ could result in **phantom tuples** appearing.
> [!Example]
> Here's an **example** where a **lossy decomposition** causes **phantom tuples**:
> * ![[Pasted image 20260413202533.png|339]]

To guarantee a **lossless split**, the two new **tables** must share a common set of [[attributes]] $X$, and this **attribute** must be a [[FDs and Keys|super-key]] for at least one of the new **tables**.
This means that if $R(A_1\dots A_n)$ has an **FD** $A_j\to A_{j+1}\dots A_n$ then **decomposing** on the **FD** to $R_1(A_1\dots A_j),R_2(A_jA_{j+1}\dots A_n)$ is **lossless**.

> [!Note]
> Adding an additional **table** can never cause a **lossless decomposition** to become **lossy**.
> 
