---
date: 2026-04-11
tags:
  - first-year
  - M40016
---
For a **single-variable function** $f(x)$, a **critical** point occurs at $x_0$ when $f'(x_0)=0$.
We determine the **nature** of the point using the second [[Differentiation|derivative]]:
* If $f''(x_0)\gt 0$ it is a local **minimum**.
* If $f''(x_0)\lt 0$ it is a local **maximum**.
* If $f''(x_0)=0$ the test is **inconclusive**, and we must check **higher-order derivatives**.

When $f''(x_0)=0$, we keep taking **derivatives** until we find the first one that does not equal $0$, $f^{(n)}(x_0)\neq 0$.
Because this is the first **non-zero term** in the function's [[Taylor series]], it dominates the others, and dictates the shape of the graph.
* If $n$ is **odd** then $(x-x_0)^n$ preserves negative signs, resulting in a **point of inflection**.
* If $n$ is **even** then we can treat it exactly like the normal **second derivative** test:
	* If $f^{(n)}(x_0)\gt 0$ it is a local **minimum**.
	* If $f^{(n)}(x_0)\lt 0$ it is a local **maximum**.