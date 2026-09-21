---
date: 2026-02-09
tags:
  - first-year
  - M40017
---
**Basis change** is the process of converting the coordinates of a [[vectors|vector]] from one [[ordered basis]] to another [[ordered basis]].

Let $B=(\overrightarrow{b_1},\overrightarrow{b_2},\dots,\overrightarrow{b_n})$ be an **ordered basis** of $\mathbb{R^n}$.
Any **vector** $\overrightarrow{x}\in\mathbb{R}^n$ can be written as a unique [[Linear Combination of Vectors|linear combination]] of the [[Basis of a Subspace|basis vectors]].
Suppose:
$$\overrightarrow{x}=\lambda_1\overrightarrow{b_1}+\lambda_2\overrightarrow{b_2}+\dots+\overrightarrow\lambda_n\overrightarrow{b_n}$$
Then we can denote its coordinate vector as:
$$\vec{x}_{w.r.t\,B}=\begin{bmatrix}\lambda_1 \\
\lambda_2 \\
\vdots \\
\lambda_n\end{bmatrix}$$
Here, $\lambda$s are the coordinates of $\vec{x}$ with respect to $B$.

Now consider two different **ordered bases**, $B$ and $D$, for the same [[Vector Spaces|vector space]] $\mathbb{R}^n$.
* $B=(\overrightarrow{b_1},\overrightarrow{b_2},\dots,\overrightarrow{b_n})$
* $D=(\overrightarrow{d_1},\overrightarrow{d_2},\dots,\overrightarrow{d_n})$
Then any vector $\overrightarrow{x}\in\mathbb{R}^n$ is a unique **linear combination** of **vectors** in $B$ and a **different** unique **linear combination** of **vectors** in $D$:
$$\vec{x}=\beta_1\vec{b_1}+\beta_2\vec{b_2}+\dots+\beta_n\vec{b_n}=\delta_1\vec{d_1}+\delta_2\vec{d_2}+\dots+\delta_n\vec{d_n}$$
$$\vec{x}_{w.r.t\, B} = \begin{bmatrix} \beta_1 \\ \beta_2 \\ \vdots \\ \beta_n \end{bmatrix} \quad \text{and} \quad \vec{x}_{w.r.t\, D} = \begin{bmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_n \end{bmatrix}$$

The **basis change** [[matrices|matrix]] $I_{BD}$ is the $n\times n$ **matrix** that changes the **basis** from $D$ to $B$.
$$I_{BD}\begin{bmatrix} \delta_1 \\ \delta_2 \\ \vdots \\ \delta_n \end{bmatrix} = \begin{bmatrix} \beta_1 \\ \beta_2\\ \vdots \\ \beta_n \end{bmatrix}  $$
That is equivalent to $I_{BD}\vec{x}_{w.r.t\,D} = \vec{x}_{w.r.t\,B}$
Note that the **vector** $\vec{x}$ has not changed, only the **coordinate system** used to locate the **vector** has changed.

We can construct this **matrix** in two ways.
Firstly, we can do it column by column, by definition.
We find the **coordinates** of the **basis vectors** $\vec{d_i}$s with respect to $B$.
These form the columns of the **matrix**:
$$\text{If } \vec{d}_i = \begin{bmatrix} \alpha_{1i} \\ \vdots \\ \alpha_{ni} \end{bmatrix}_{w.r.t \ B}\forall i\in\{1,2,\dots,n\} \quad \text{then} \quad I_{BD} = \begin{bmatrix} \alpha_{11} & \dots & \alpha_{1n} \\ \vdots & & \vdots \\ \alpha_{n1} & \dots & \alpha_{nn} \end{bmatrix}$$

An easier way is using the [[standard ordered basis]].
If $E$ is the **standard ordered basis**, then we can easily construct $I_{EB}$ and $I_{ED}$ by using the **basis vectors** as columns:
* Since $\vec{x}=\beta_1\vec{b_1}+\beta_2\vec{b_2}+\dots+\beta_n\vec{b_n}$
* We can write this as a **matrix multiplication** $\vec{x}=\begin{bmatrix}\vec{b_1} & \vec{b_2} \dots & \vec{b_3}\end{bmatrix}\begin{bmatrix}\beta_1\\\beta_2\\\vdots\\\beta_n\end{bmatrix}$
* Which is the same as $\vec{x}=I_{EB}\vec{x}_{w.r.t\,B}$
* So $I_{EB}=\begin{bmatrix}\vec{b_1} & \vec{b_2} &\dots & \vec{b_n}\end{bmatrix}$ 

**Basis change matrices** have two useful properties:
*  They are **invertible**, since they are square, and by definition a [[Basis of a Subspace|basis]] consists of [[Linear Independence|linearly independent]] **vectors**.
	* This means that the reverse **basis change** is simply the **inverse** of the matrix.
	* $I_{AB}=(I_{BA})^{-1}$ 
* They can be **composed**, simply by **matrix multiplication**.
	* $I_{AC}=I_{AB}I_{BC}$


Now we can construct $I_{BD}$ using $I_{EB}$ and $I_{ED}$ easily, as follows:
$$I_{BD}=I_{BE}I_{ED}=I_{EB}^{-1}I_{ED}$$
In full, this is:
$$I_{BD}=\begin{bmatrix}\vec{b_1} & \vec{b_2} & \dots & \vec{b_n}\end{bmatrix}^{-1}\begin{bmatrix}\vec{d_1} & \vec{d_2} & \dots & \vec{d_n}\end{bmatrix}$$
Where $\vec{b_1}, \vec{b_2},  \dots , \vec{b_n}$ are the **basis** vectors of $B$ and $\vec{d_1}, \vec{d_2},  \dots , \vec{d_n}$ are the **basis** vectors of $D$.