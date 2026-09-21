---
date: 2025-12-30
tags:
  - first-year
  - haskell
  - M40009
---
The [[Monads|Monad]] laws are **unital return** and **associative `(>>=)`**:
```Haskell
return x >>= f = f x

p >>= return = p

(p >>= f) >>= g = p >>= (\x -> f x >>= g)
```

Equivalently in **do-notation**:
```Haskell
do 
	x <- p 
	return x
=
p

do 
	x <- return y 
	p x
= 
p y

do (p ; q) ; r = do p ; (q ; r) = do p ; q ; r 
```
