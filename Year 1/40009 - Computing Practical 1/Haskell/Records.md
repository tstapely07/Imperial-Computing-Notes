---
date: 2025-12-21
tags:
  - first-year
  - haskell
  - M40009
---
A **person** has a **name**, **age**, and **height**.
We can construct a [[User-Defined Datatypes|datatype]] for this:
```Haskell
data Person = Person String Int Double
```
>[!Example]
>```Haskell
>tom = Person "Tom" 128 "1.83"
>```

If we have a **person** and want to extract the **name**, **age**, or **height**, we can write functions to [[Pattern Matching|pattern match]] on the `Person` constructor.#
```Haskell
name :: Person -> String
name (Person n _ _) = n

age :: Person  -> Int
age (Person _ a _) = a

height :: Person -> Double
height (Person _ _ h) = h
```
But this is **tedious**. 

**Record syntax** is a better  way of writing this sort of structured data:
```Haskell
data Person = Person {
	name :: String,
	age :: Int,
	height :: Double
}
```
This says that a `Person` has three **fields**, `name :: String`, `age : Int`, and `height :: Double`.
>[!Success]
>This fields give us the functions from before **for free**.
>>[!Example]
>>```
>>Haskell
>>anish = Person { "Anish", "18", 1.75 }
>>age anish = 18 
>>```

**Record syntax**  brings other features:
We can **specify** the **fields**:
```Haskell
seb = Person { name = "Seb", age = "18", height = 1.89 }
```

We can write a [[Types, Values, and Functions|function]] to **copy** and **alter** a **record**:
```Haskell
birthday :: Person -> Person
birthday person = person { age = age person + 1 }
```

>[!Warning]
>Do not try and use records for an **object-oriented** style.
>It's  just not what they're designed for.


