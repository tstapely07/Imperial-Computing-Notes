---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
Here's an implementation of an exponentiation function.
```Haskell
power :: Int -> Int -> Int
power 0 x = 1
power n x = x * power (n-1) x
```
We can make this function better by using **exponentiation by squaring**.
We know that:
	$$\begin{align*}
	x^{2k} &=n^k*n^k \\
	x^{2k+1} &=n*n^k*n^k
	\end{align*}$$
Now we can write:
```Haskell
power :: Int -> Int -> Int
power n 0 = 1
power n k
	| even k = power n (k `div` 2) * power n (k `div` 2)
	| otherwise = n * power n (k `div` 2) * power n (k `div` 2)
```
> [!Warning]
> The problem here is that the computation `power n (k 'div' 2)` multiple times. 

To solve this, we can rename the clause, and then reuse the variable:
```Haskell
power :: Int -> Int -> Int
power n 0 = 1
power n k
	| even k = x * x
	| otherwise = n * x * x
	where 
		x = power n (k `div` 2)
```
>[!Info]
>The **order** of definitions in a `where` doesn't matter.

>[!Warning]
>The variables defined in a `where` clause are **only in scope** for the function clause that they are defined in.




