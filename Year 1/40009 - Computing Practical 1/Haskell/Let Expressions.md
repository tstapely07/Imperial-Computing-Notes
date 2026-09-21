---
date: 2025-12-21
tags:
  - first-year
  - "#haskell"
  - "#M40009"
---
**Let expressions** are an alternative to **[[Where Clauses|where clauses]]**.
They can be found **anywhere** that an **expression** can be found.
They are most commonly used to break down a **complex expression** into more **readable parts**:
```Haskell
calculateCylinderArea :: Double -> Double -> Double
calculateClyinderArea r h = 
	let sideArea = 2 * pi * r * h
		topArea = pi * r * r
	in  sideArea + 2 * topArea
```

>[!Info]
**Let  expressions** allow **more precise scoping** than **[[Where Clauses|where clauses]]**.
Values defined within can be seen between the `let` and `in`, as well as in the expression after the `in`.
