---
date: 2025-12-30
tags:
  - first-year
  - M40009
  - haskell
---
`IO a` is a [[Parameterised Data Types|type]] which **abstracts programs** of type `a` that **interact** with the outside world.
The available operations include:
```Haskell
putStrLn :: String -> IO ()
print :: Show a => a -> IO ()
writeFile :: FilePath -> String -> IO ()
```
These [[Types, Values, and Functions|functions]] take an **argument** and return an `IO ()` - "IO unit".
These are programs that **return no result**.

>[!Info]
>To keep Haskell **pure**, there is no function like:
>```Haskell
>unsafeExtract :: IO a -> a
>```
>This means that we **cannot leave** `IO`.
>The only way to work with it is using its [[Functors|functor]], [[Applicatives|applicative]] or [[Monads|monad]] interface.
>This keeps the **pure** program logic safe from **side effects**.

The **top-level** function for any program is called `main`:
```Haskell
main :: IO ()
main = putStrLn "hello world"
```
Or:
```Haskell
main :: IO ()
main = do 
	putStrLn "Hello"
	putStrLn "These are..."
	putStrLn "...seperate lines"
```

We can do more than just output:
```Haskell
getChar :: IO Char
getLine :: IO String
readFile :: FilePath -> IO String
```
These are all `IO` but they return something that isn't `()`.
Now we can do:
```Haskell
main = greet
greet :: IO ()
greet = do
	putStrLn "Hello, what's your name?"
	name <- getLine
	putStrLn ("Hey " ++ name ++ ", nice to meet you!")	
```

Here's a final example:
```Haskell
ageGroup :: Int -> IO ()
ageGroup age
	| age < 11 = putStrLn "You are a child"
	| age < 18 = putStrLn "You are a teenager"
	| age < 25 = putStrLn "You are a young adult"
	| age < 65 = putStrLn "You are a adult"
	| otherwise = putStrLn "You've been around for a while"
	
converse :: IO ()
converse = do
	putStrLn "How old are you?"
	age <- read <$> getLine
	ageGroup age
	
main = converse
```


