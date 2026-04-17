---
date: 2026-02-16
tags:
  - first-year
  - M40008
---
In **dynamic programming**:
* The **main problem** is broken down into **subproblems**, which are **overlapping**.
* In contrast to [[divide and conquer algorithms]], which deal with **independent subproblems**, the same **subproblem** can repeat multiple times.

There are two main approaches to **dynamic programming**.

In the **top-down** approach we use **memoisation**:
* We start from the **main problem**, and use **recursion** to break it down.
* To avoid redundant work, we use a **memo** to store the results from **subproblems**.
* When a **subproblem** is reached, we first check the **memo** to see if it has already been solved.
* We only need to solve the **subproblem** from scratch if it has not already been solved.
A **top-down** approach is **lazy**, since it only solves **subproblems** if their solutions are actually needed for the **main problem**.

In the **bottom-up** approach:
* The **main problem** is broken down into **subproblems**, which are then ordered, e.g. by increasing size, with the final **subproblem** being the original **main problem**.
* We then start at the **first subproblem** and move through the **subproblems** in order.
* We solve each **sub-problem** using the stored solutions of the previous **subproblems**, and store the new solution for later use.
* Finally, in solving the final **subproblem**, we solve the **main problem**.
Two examples of **bottom-up dynamic programming** are [[Warshall's algorithm]] and [[Floyd's algorithm]].

> [!Example]
> Let's solve the same **problem** twice, to demonstrate both approaches.
> Can a string `s` be split into words that occur in a dictionary?
> * For example, if `s="windown"`, then two solutions could be `"win down"` or `"wind own"`.
> * If `s="trcalenz"`, then there are no valid solutions.
> 
> A **top-down** approach has the following **python-like pseudocode**:
> ```Python
> def wordBreak1(s):
> 	if len(s) == 0: 
> 		return True
> 	else:
> 		for i in range(0, len(s)):
> 			if inDict(s[i:]):
> 				if wordBreak1(s[:i]):
> 					return True
> 	return False
> ```
> The **recurrence relation** in the [[Worst Case vs Average Case Analysis|worst case]] is:
> $$\begin{gather}
> W_1(0)=0\\
> W_1(n)=n+W_1(0)+\dots+W_1(n-1)
> \end{gather}$$
> Which gives $W_1(n)=2^n-1$, **exponential** [[Orders of Complexity|complexity]].
> * This arises from repeatedly calculating identical substrings in the recursive call.
> We can improve this by using **memoisation**:
> * In **python**, this is done using a **dictionary**.
> ```Python
> memo = {}
> def wordBreak2(s):
> 	if len(s) == 0: 
> 		return True
> 	else:
> 		for i in range(0, len(s)):
> 			if inDict(s[i:]):
> 				if s[:i] not in memo:
> 					memo[s[:i]] = wordBreak2(s[:i])
> 				if memo[s[:i]]:
> 					return True
> 	return False
> ```
> Now, for a string of length $n$, there are only $n$ unique **subproblems**, all the prefixes.
> * Since solving each **subproblem** takes $O(n)$ [[Formal Definitions of Big-O and Big-Theta|time]], the total complexity is now $O(n^2)$.
> 
> Here's the **python-like pseudocode** for the **bottom-up** approach:
> ```Python
> def wordBreak3(s):
> 	n = len(s)
> 	wb[0] = True # base case
> 	if n > 0:
> 		for i in range(1, n+1): # 1 to n
> 			wb[i] = False
> 			for j in range(0, i): # 0 to i-1
> 				if wb[j] and indict(s[j:i]):
> 					wb[i] = True
> 					break
> 	return wb[n]
> ```
> With a nested for loop, the **time complexity** here is clearly also $O(n^2)$.

