---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
> [!Note]
> **Floating point** in [[binary]] is just like **standard form** in **decimal**.

A **floating point number** consists of two parts:
$$\text{coefficient}\times 2^\text{exponent}$$
* The **coefficient/significand/mantissa**. 
	* Here, more **bits** increases **precision**.
* The **exponent/characteristic**.
	* Here, more **bits** increases the **range**.

**Floating point** numbers are **normalised** to ensure each number has a unique representation.
* We mandate that there must always be a single $1$ placed before the **binary point** (apart from for $0$).
* This $1$ is therefore implied, and can be dropped, to save a **bit**.

**Floating point arithmetic**:
* For **addition**, we shift one number until the exponents are the same, and then add the **coefficients**.
	* The **exponent** is unchanged.
* For **multiplication**, we **multiply** the **coefficients** and add the **exponents**.

When the result of an operation is too large to be stored in the **coefficient**, we can resolve the error in two ways:
* **Truncation** always rounds down, and is a **biased** error.
* **Rounding** is an **unbiased** error.

Exponent **overflow** occurs when the result is too large.
* i.e. the **exponent** is greater than the **maximum exponent**.
* This is handled by setting the value as infinity, or raising an **exception**.
Exponent **underflow** occurs when the result is too small.
* i.e. the **exponent** is smaller than the **minimum exponent**.
* This is handled by setting the value as 0, or raising an **exception**.
Note that a **rounding** error, where precision is lost, is different to an **overflow** or **underflow** error.

Since **floating point** can result in inexact results, we should account for results that are sufficiently close when testing equality.
* One approach is checking within some fixed bound: $a=b \equiv (b-\epsilon)\lt a\lt (b+\epsilon)$.
* A more general approach is calculating the bound based on the relative size of the numbers being compared.

The **IEEE** defines a widely adopted floating point standard, including:
* How the **coefficient** and **significand** should be stored in memory.
* **Semantics** of **arithmetic** operations.
* Rules for **error conditions**.

**Single precision** (32-bit):
* Often used when memory is limited.
* 1 **sign bit**, 8 **exponent bits**, 23 **significand bits**.
* The $1.$ is omitted.
* The **exponent** is stored as an [[Signed Integers#^d3d41b|excess-127]] value, allowing non-negative numbers to be easily compared.
* The value represented is therefore $\pm 1.F\times 2^{E-127}$.
* The range that can be represented is approximately $-10^{38}$ to $-10^{-38}$, 0, $10^{-38}$ to $10^{38}$ .

**Double precision** (64-bit):
* 1 **sign bit**, 11 **exponent bits**, 52 **significand bits**
* The **exponent** is stored as an **excess-1023** value.
* Value represented is $\pm 1.F*2^{E-1023}$.
* Normalized ranges in decimal are approximately $-10^{308}$ to $-10^{-308}$, 0, $10^{-308}$ to $10^{308}$ .

The **IEEE** uses specific bit patterns to encode special states:
*  Denormalised numbers and $0$:
	* These are represented by a **coefficient** of all zeros.
	* By allowing many $0$s after the point, before the first $1$, denormalised numbers can represent numbers between the underflow limits and zero.
	* Of course, a **significand** of $0$ represents $0$.
* An **exponent** of all $1$s and a **significand** of $0$ represents **infinity**.
	* This occurs in **overflow** or division by zero.
	* Note that something like $\infty+5=\infty$ or $\infty +\infty=\infty$ is valid.
* An **exponent** of all $1$s and a non-zero **significand** represents NaN.
	* NaN occurs from operations with no valid interpretation, such as $\infty -\infty$ or $\frac{0}{0}$.