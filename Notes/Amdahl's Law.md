---
date: 2026-04-16
tags:
  - first-year
  - M40005
---
**Amdahl's law** defines the **theoretical maximum** [[performance]] **improvement** achieved by only **optimising** a **part** of the **system**.
* If a program takes an initial time of $T_{old}$, and we speed up some fraction $\alpha$ by a factor of $\beta$ the new execution time is calculated as:
$$T_{new}=\frac{\alpha T_{old}}{\beta}+(1-\alpha)T_{old}$$

> [!Example]
> For example, creating a **custom** **instruction** to speed up $90\%$ of a **program** by $100$ times, the new **execution** **time** will be:
> $$T_{new}=(\frac{0.9}{100}+(1-0.9))T_{old}=0.109T_{old}$$
> This means the new **program** will only be $\frac{1}{0.109}\approx9.2$ times faster.