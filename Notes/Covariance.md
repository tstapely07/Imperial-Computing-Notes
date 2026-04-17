---
date: 2026-03-11
tags:
  - first-year
  - M40017
---
**Covariance** measures how two **variables** change together.
* These could be two **axes** or [[Dimension|dimensions]] of the dataset.
For a sample of $n$ datapoints, the **covariance** of two random variables $X$ and $Y$ is:
$$\operatorname{cov}(X,Y)=\frac{1}{n-1}\sum_{j=1}^n(x_j-\bar{x})(y_j-\bar{y})$$
* Where $\bar{x}$ and $\bar{y}$ are the **means** of $X$ and $Y$. 

Note that by applying the [[Cauchy-Schwarz inequality]], and using the fact that the **covariance** of a **variable** with itself is just its **variance**, we can bound the **covariance**:
$$\operatorname{cov}(X,Y)^2\le\operatorname{cov}(X,X)\operatorname{cov}(Y,Y)=\operatorname{var}(X)\operatorname{var}(Y)$$

For a dataset with many **dimensions**, we construct the **covariance matrix** $[\operatorname{cov}]$ where the **element** in the $r^{th}$ **row** and the $c^{th}$ **column** is $\operatorname{cov}(X_r,X_c)$
* Because $\operatorname{cov}(X_r,X_c)=\operatorname{cov}(X_c,X_r)$, the **covariance matrix** is always **symmetrical**, so $[\operatorname{cov}]=[\operatorname{cov}]^\top$.
* By the [[Spectral theorem]], all [[Eigenvectors and Eigenvalues|eigenvalues]] of the **covariance matrix** are real numbers.
	* The proof is omitted for brevity, but the **eigenvalues** are also **non-negative**.
* Each **eigenvalue** represents the **variance** of the data along its corresponding **eigenvector**.
	* A larger **eigenvalue** means the data is widely spread in that direction.
	* A smaller **eigenvalue** means it is narrowly spread.