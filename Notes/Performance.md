---
date: 2026-04-15
tags:
  - first-year
  - M40005
---
**CPI** stands for **cycles per instruction**.
* Since different **instructions** require different numbers of [[Clocks|cycles]], CPI is always calculated as an average across all the **instructions** in a given **program**.

We can define the **execution time** for a **program** as:
$$\text{execution time} = \text{instruction count}\times \text{CPI}\times \text{clock cycle time}$$
* Where $\text{clock cycle time}=\frac{1}{\text{clock speed}}$

We can therefore compare the **performance** of two **processors** by comparing their **execution times** for a given **program**.

The different aspects that contribute to **execution time** are affected by different factors, as shown in this table:
* ![[Pasted image 20260415122302.png|448]]

Compare to **CISC**, the [[RISC-V Architecture|RISC]] [[Instruction Set Architecture (ISA)|ISA]] reduces both **CPI** and **cycle time**, since a smaller number of **instructions** allows for better **hardware optimisation**.
* However, since **RISC** has simpler instructions, a given program requires a higher **instruction count** then the same program in a **CISC ISA**.
* An optimised **compiler** can help reduce this **instruction count**.
* Overall, **RISC** does still offer better performance over **CISC**.

**Benchmarking** is a way to evaluate a processor's performance.
We can benchmark on three different workloads:
* Using the **actual target workload** is highly **representative**, but it is highly **specific** and not **portable**.
	* It can also be hard to identify **specific problems**
* **Full** **application** **benchmarks** are **portable** and **widespread**, but are less **representative** than the using the **target** **workload**.
* **Small** **kernel** **benchmarks** are **easy** to use, especially **early** in the **design** **cycle**, and can help identify **peak performance**, but are not very **representative**, since **peak** **performance** is often far from **typical** **performance**.