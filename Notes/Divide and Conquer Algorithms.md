---
date: 2026-03-03
tags:
  - first-year
  - M40008
---
The **divide and conquer** paradigm breaks down a larger problem into smaller problems, solves them, and then stitches the answers back together.
There are generally three distinct steps:
* **Divide**: divide the main problem into $a$ **subproblems**, each of size $n/b$.
	* Setting up these subdivisions might require its own computational work.
* **Solve**: solve each of the **subproblems** recursively until a base case is reached.
* **Combine**: combine the results of the **subproblems** to get the final answer.
	* Just like dividing, combining often also requires additional computational work.

One example of a **divide and conquer** algorithm is [[Strassen's algorithm]].
* It divides the problem into $a=7$ subproblems of size $n/2$.
* Both the **divide** and **combine** steps require extra work, in the form of **matrix** **additions** and **subtractions**.

Other examples, include the [[Merge Sort]] and the [[Quick Sort]].
