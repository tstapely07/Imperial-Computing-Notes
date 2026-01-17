---
date: 2026-01-13
tags:
  - first-year
  - M40005
---
There are multiple measures of performance, but in our case, we solely care about **speed**.
We require:
* A method for calculation.
* A basis for comparison.
* A metric for evaluation.
* An understanding of implications for architectural choices.

Almost all computers have a clock that determines when events take place in the hardware. 
These discrete time intervals are called clock signals.
When we talk about clock or cycles, we refer to the clock cycle, and clock period is the same as cycle time.
When we talk about frequency and clock frequency we mean the clock rate.

The term CPI - clock cycles per instruction, is the average number of clock cycles each instruction takes to execute.
Since different instructions may take different amounts of time, CPI is an average of all the instructions executed in a program.
CPI provides a way of comparing two different implementations of the same ISA, since the number of instructions executed for a program is the same.

The execution time of a program is therefore the product of instruction count, the CPI, and the cycle time.
Execution time is our chosen measure for performance, rather than other measures such as clock frequency.

![[Pasted image 20260113152358.png|400]]
![[Pasted image 20260113152413.png|400]]


There are multiple aspects that affect processor performance:
![[Pasted image 20260113152907.png|400]]
The algorithm determines the number instructions from the source program, and hence the instruction count. 
The algorithm may also affect the CPI, by favouring faster or slower instructions, e.g. divide has a higher CPI than add, subtract and multiply.

The programming language affects instruction count, since statements in the language are translated to processor instructions, which determine instruction count.
The language may also affect the CPI because of its features, for example a language with heavy support for data abstraction, such as Java, will require indirect calls, which will often use instructions with higher CPI.

The efficiency of the compiler affects both the instruction count and the average cycles per instruction, since the compiler determines the translation of the source language instructions into computer instructions. 
The compiler's role can be very complex, and affect the CPI in complex ways.

The instruction set architecture affects all three aspects of CPU performance, since it affects the instructions needed for a function, the cost in cycles for each instruction, and the clock rate of the processor.

The machine organisation, and the transistor technology only affect the clock rate.


Let's compare [[Instruction Set Architecture|RISC and CISC architectures]]:
![[Pasted image 20260113154525.png|400]]
Although the cycle time and the instruction count of the RISC are worse than those of the CISC, its lower CPI enables higher performance.
Additionally, the cost is only up to 20% more, for double the performance.

![[Pasted image 20260113154637.png|400]]
We can see that the biggest strength of RISC is the low CPI compared with CISC, which reflects the simple and regular instruction format.
Note that RISC does still have drawbacks, such as the large code size.

There are other ways to improve performance:
![[Pasted image 20260113154736.png|400]]


![[Pasted image 20260113155126.png|400]]
Evaluating performance is necessary, since performance can guide design decision, and help compare architectures and their implementations.
Benchmarking is a systematic way to evaluate performance.

There are three main methods for performance evaluation:
![[Pasted image 20260113155239.png|400]]
