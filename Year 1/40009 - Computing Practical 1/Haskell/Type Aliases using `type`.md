---
date: 2025-12-29
tags:
  - first-year
  - haskell
  - M40009
---
`type` is used to create **shorthand** for **complex types**.
Unlike [[Newtypes|newtype]]  and [[User-Defined Datatypes|data]], it **doesn't** create a new type.
It only gives an existing type an **alternative name**.
>[!Example]
>```Haskell
>type Username = String
>type Age = Int
>type Email = String
>type User = (Username, Age, Email)
>
>findUser :: [User] -> Username -> User
>```
>Is **more readable** than:
>```Haskell
>findUser :: [(String, Int, String)] -> String -> (String, Int, String)
>```

We use `type` over `newtype` when we **want** to the types to be **interchangeable**.
This lets us use functions defined on the **base type** without having to **wrap and unwrap** the data.

We can also use `type`to **pre-fill** parameters of a [[Parameterised Data Types|parameterised data type]]:
```Haskell
type Result a = Either string a
```
Now we could write:
```Haskell
validateNum :: Int -> Result Int
```

