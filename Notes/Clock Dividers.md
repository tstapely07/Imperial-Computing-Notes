---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
A [[Synchronous Circuits|synchronous]] divide-by-two circuit uses a single [[Edge-Triggered D-Type Flip-Flop|edge-triggered D-type flip-flop]], where the input is taken directly form the inverted output.
* This means that the **flip-flop** changes state on every **falling-edge**, and so outputs a wave at half the frequency of the original [[Clocks|clock]].
* ![[Pasted image 20260409121921.png|300]]
* ![[Pasted image 20260409121931.png|366]]

To **divide** by any integer, we can easily define a [[Sequential Circuits|sequential circuit]] to do so.
For example, division by $7$ could be achieved by this [[Finite State Machines|finite state machine]]:
* ![[Pasted image 20260409122036.png|260]]
Although the resulting **clock signal** would be slightly unbalanced, this shouldn't matter, since most components are only **edge-triggered**.

To divide by very large numbers would require **many states**, and therefore a large [[Synchronous Binary Counters|binary counter]].
To solve this, we can simply chain two **dividers**:
* ![[Pasted image 20260409122744.png|439]]
* The circuit is now [[Asynchronous Circuits|asynchronous]], so clearly is a trade off.
Going further, a very simple **asynchronous counter** is the **ripple through counter**, created by chaining basic divide-by-two **flip-flops**:
* ![[Pasted image 20260409122912.png|403]]
* This removes the need for any complex state sequencing logic.

To divide by a number that isn't a power of two, if designing an **FSM** is unrealistic, we can simply add **clear** functionality to a **ripple counter**.
* We take a **ripple counter** that counts to the next higher power of $2$.
* When the number we wish to count to is reached, we simply use the **clear** input of the **flip-flop** to reset the stored **bit** to $0$.
* For example, to divide by $5$, we take a **ripple counter** that counts to $8$, but reset it to $0$ as soon as the output reaches $5$.
Here is the **asynchronous circuit** for division by $5$:
* ![[Pasted image 20260409123339.png|439]]