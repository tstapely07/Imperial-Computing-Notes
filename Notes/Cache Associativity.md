---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
**Associativity** dictates how flexible the [[x86 Cache|cache]] is when deciding where to place a **block** of **data**.
* Each **address** maps to a single **set**, but each **set** can store a **block** in more than one way.

In **direct-mapped cache**, each **set** only stores a single **line**, and therefore a single **block**.
In an $N$-**way set associative cache**, each **set** has multiple **lines**, $N$.
In a **fully associative cache**, the entire **cache** is a single **set**, and so a block can be placed **anywhere**.

Now, the number of **sets** is $\frac{C}{B\times N}$, so the number of [[Binary|bits]] used to identify the **set** is $I=\log_2(\frac C {B\times N})$.
* As the **associativity** **increases**, we need fewer **bits** to identify the **set**, so $I$ can shrink. However, we now need a longer tag to differentiate between the **blocks**.
* ![[Pasted image 20260420183133.png|364]]

> [!Example]
> For example, let's look where the **address** `0x1833` would be placed, with three different **associativities**.
> * Let's use a $16$-**byte** **block** **size**, with $8$ **blocks**, and $16$ bit **addresses**.
> In **binary**, we have `0b 0001 1000 0011 0011`. 
> * For **direct-mapped**, we need $3$ **bits** for the **index**, so `011`, and we store the **block** in **set** $3$.
> * For $2$-**way set associative**, the **index** is $2$ **bits**, so `11`, so store the **block** in either of the two places in **set** $3$.
> * For $4$-**way set associative**, the **index** is $1$ **bit**, so `1`, so store the **block** in any of the places in **set** $1$.
> * ![[Pasted image 20260420183506.png|336]]

Any **empty block** in the given **set** can be used to store the **block**.
* If there are no **empty** **blocks**, then we generally choose the **least** **recently** **used** (**LRU**) **block**.
* Note that for **directed-mapped caches** we do not get a choice which **block** to replace.

When the **CPU** reads the **cache**, it first uses the **index** ($I$) bits to find the correct **set**.
* It then checks if any **line** in that **set** has a **tag** that matches the **address** requested.
	* In an $N$-**way** **associative** **cache**, all **tags** are compared **simultaneously**.
* If the **tag** matches and the **valid** **bit** ($V$) is a $1$, it is a **hit**.
	* The **valid** **bit** is necessary to avoid cases where the **tag** matches by chance.
* We can then we use the **offset** ($O$) bits to locate the specific **byte** within the **block**.

We can classify **cache misses** into three types:
* **Compulsory** (**cold**) **misses** occur on the very first access to a **block**.
* **Conflict misses** occur when the **cache** is large enough, but multiple data objects map to the same **set**, and so they constantly **evict** each other.
	* **Direct mapped caches** suffer from **conflict** **misses** the most.
	* **Fully associative caches** don't suffer from **conflict** **misses** at all, since it would be considered a **capacity** **miss**.
* **Capacity** **misses** occur when the set of **active** **cache** **blocks**, the **working** **set**, is larger than the **cache**.

On a **write hit**, the **CPU** has two options:
* **Write-through**:
	* Write immediately to **memory** and all **caches** in between.
	* This ensures **memory** is always consistent with the **cache** **copy**, but is **slower**.
* **Write-back**:
	* Defer the **write** to **memory** until the **cache** **line** is **evicted**.
	* A **dirty** **bit** is required to indicate the **line** has been modified.
	* This is much **faster**, but more **complex**.

Similarly, on a **write miss** the **CPU** has two options:
* **Write-allocate**:
	* Load the block from **memory** into the **cache** first, and then update it.
	* This is more complex, and may **evict** an existing **block**, but is faster if more **writes** to the same **location** happen next.
	* This is usually paired with **write-back**.
* **No-write-allocate**:
	* Bypass the **cache** and write directly to **memory**.
	* This is very **slow** if the same **value** is written to multiple times.
	* This is usually paired with **write-through**.

