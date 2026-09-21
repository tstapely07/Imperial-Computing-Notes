---
date: 2025-12-13
tags:
  - first-year
  - haskell
  - M40009
---
We can define functions so that they inspect the input to decide what to do next.
```Haskell
dirac :: Integer -> Integer
dirac 0 = 1
dirac n = 0
```
`n` matches any integer

Alternatively, we could define a factorial function:
```Haskell
fact :: Integer -> Integer
fact 0 = 1
fact 1 = 1
fact 2 = 2
fact 3 = 6
fact n = n * fact (n-1) 
```
`n` can be used in the function body.
This is a [[Recursive Functions|recursive function]], because it is defined in terms of itself. 


>[!Tip]
> [[Lists#^0b6000|Pattern matching over lists is possible, and very powerful]].

>[!Warning]
>Pattern matching creates the possibility of a function where not all inputs have a definition. Functions like these are dangerous, and are called **partial functions**.

^51a9f1
>[!Info]
>We may want to **pattern match** over the **result** from a **[[Types, Values, and Functions|function]]**.
>One way to do this would be using a **[[Helper Functions|helper function]]**, in a **[[Where Clauses|where clause]]**.
>Alternatively, we could use a **[[Case Expressions|case expression]]**.



