---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
To connect [[Static RAM|RAM]] to a processor, we require some new [[registers]]:
* The **memory address register** (**MAR**) stores the **address** in **memory** to be written to or read.
* The **memory data/buffer register** (**MDR/MBR**) stores the **data** read from **memory**, or the **data** to be **written** to **memory**.
* The **program counter** (**PC**) stores the **address** of the next **program instruction** to be executed.
* The **instruction register** (**IR**) stores the **program instruction** being executed.

The **memory** side of the connection looks like this:
* ![[Pasted image 20260412112905.png|302]]
The **processor** side of the connection looks like this:
* ![[Pasted image 20260412113003.png|307]]
Together, we have the final connection:
* ![[Pasted image 20260412113030.png|326]]