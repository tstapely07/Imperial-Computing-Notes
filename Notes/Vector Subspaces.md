---
date: 2026-01-21
tags:
  - first-year
  - M40017
---

> [!Abstract] Definition
> A **vector subspace** is a subset of a [[Vector Spaces|vector space]], which is a **vector space** in itself.

If $(V,\oplus,\otimes,\overrightarrow{0})$ is a **vector space**, then if $S\subseteq V$ such that $(S,\oplus,\otimes,\overrightarrow{0})$ is a **vector space**, then $S$ is a **subspace** of $V$.

>[!Note]
>The **subspace** must use the **same operations** as the **original space**.

Let's do some **examples**:
$$\begin{gather}
\text{Is }A=\{\lambda,\lambda+\mu^3,\lambda-\mu^3 \; | \; \lambda,\mu\in\mathbb{R}\} \text{ a subspace of } \mathbb{R}^3\text{?} \\\\
\text{take } \overrightarrow{x}=\begin{bmatrix} \lambda_1 \\ \lambda_1+\mu_1^3 \\ \lambda_1-\mu_1^3\end{bmatrix},\overrightarrow{y}=\begin{bmatrix} \lambda_2 \\ \lambda_2+\mu_2^3 \\ \lambda_2-\mu_2^3\end{bmatrix}\in A \\
\overrightarrow{x} + \overrightarrow{y} = \begin{bmatrix}\lambda_1+\lambda_2 \\ (\lambda_1+\lambda_2)+\left(\sqrt[3]{\mu_1^3+\mu_2^3}\right)^3 \\  \\
(\lambda_1+\lambda_2)-\left(\sqrt[3]{\mu_1^3+\mu_2^3}\right)^3\end{bmatrix} \in A \\\
\text{if } \lambda = \lambda_1+\lambda_2,\;\mu=\sqrt[3]{\mu_1^3+\mu_2^3} \\
\text{so closed under vector addition} \\ \\
\gamma\in\mathbb{R}\\
\gamma\overrightarrow{x} = \begin{bmatrix} \gamma\lambda_1 \\ \gamma\lambda_1+\gamma\mu_1^3 \\ \gamma\lambda_1-\gamma\mu_1^3\end{bmatrix} \in A \\
\text{if } \lambda = \gamma\cdot\lambda_1,\;\mu=\sqrt[3]{\gamma}\cdot\mu_1 \\
\text{so closed under scalar multiplication} \\\\
\text{so A is a subspace}
\end{gather}$$

Here's an interesting example:
$$\begin{gather}
\text{Let } \gamma\in\mathbb{R} \\
\text{Is }C=\{(\xi_1,\xi_2,\xi_3)\in\mathbb{R}^3\;|\; \xi_1-2\xi_2+3\xi_3 = \gamma\}\text{ a subspace of }\mathbb{R}^3\\
\begin{bmatrix} x \\ y \\ z \end{bmatrix},x-2y+3z=0 \\
\overrightarrow{x}=\begin{bmatrix} x_1 \\ y_1 \\ z_1 \end{bmatrix},\overrightarrow{y}=\begin{bmatrix} x_1 \\ y_1 \\ z_1 \end{bmatrix}\in C \\
\text{So } x_i-2y_i+3z_i = \gamma \text{ for }i=1,2\\
\overrightarrow{x}+\overrightarrow{y}=\begin{bmatrix}x_1+x_2 \\ y_1+y_2 \\ z_1+z_2\end{bmatrix} \\
\text{Check condition: } (x_1+x_2)-2(y_1+y_2)+3(z_1+z_2) \\
= (x_1-2y_1+3z_1)+(x_2-2y_2+3z_2) \\
= \gamma + \gamma = 2\gamma \\
\text{We need } 2\gamma=\gamma, \text{ so only closed under addition for } \gamma = 0
\end{gather}$$
>[!Info]
>This tells us that the **solution set** of a **homogenous** [[Systems of Linear Equations|system of linear equations]] is a **subspace** of $\mathbb{R}^n$, which is in turn equivalent to the [[Vector Span|span]] of some set of [[Vectors|vectors]].
 >
>Conversely, the **solution set** to a **non-homogenous system of linear equations** cannot be a **subspace** of $\mathbb{R}^n$, since it will not contain the 0-vector $\overrightarrow{0}$.


> [!Info]
> See also [[Basis of a Subspace]]



