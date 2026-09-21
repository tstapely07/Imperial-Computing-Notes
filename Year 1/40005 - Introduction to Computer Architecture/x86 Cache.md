---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
**Cache** is **computer memory** with a **short access time** used for the storage of frequently or recently used [[Instruction Format|instructions]] or **data**.

[[x86 Memory Layout|Main memory]] can be viewed as being partitioned into fixed-size **blocks**, or **lines**.
* The **cache** holds a small **subset** of these **memory blocks** at any given **time**.
* ![[Pasted image 20260420165822.png|320]]
* ![[Pasted image 20260420165845.png|317]]
When the **CPU** accesses a [[Memory Addressing Modes|memory address]], the entire **block** containing that **address** is copied into the **cache**.
* This takes advantage of [[Principle of Locality|locality]].

When the **CPU** requests a **memory address**, the **cache** checks if it already has the **block** containing that **data**. 
There are two **possibilities**:
* If the **data** is found in the **cache**, then we have a **cache** **hit**.
* If the data is not in the **cache**, we have a **cache** **miss**, and the **CPU** is forced to pause while the **block** is fetched from **main** **memory**.
When a **cache miss** occurs, two decisions must be made:
* Where the new **block** should be stored, the **placement policy**.
* If the **cache** is **full**, which block **should** be evicted to make room. This is the **replacement policy**.

We can measure [[performance]] using **three variables**:
* **Hit time** (**HT**) - the **time** it takes to check the **cache** and deliver the **block** to the processor.
* **Miss rate** (**MR**) - the **fraction** of requests that are not found in **cache**.
	* Note there is also **hit** **rate**, defined as $1-\text{miss rate}$
* **Miss** penalty (**MP**) - the **additional** **time** required to fetch the data from **main** **memory** after a **cache** **miss**.

We define the **average memory access time** (**AMAT**) as:
$$\text{AMAT}=\text{HT}+\text{MR}\times\text{MP}$$
This shows us that, since the **miss penalty** is so large, a small change in **hit rate** has a large impact.
* Assume the **hit time** is $1$ **cycle**, and the **miss penalty** is $100$ **cycles**.
* With a $97\%$ **hit rate**, $\text{AMAT}=1+(0.03*100)=4\text{ cycles}$.
* With a $99\%$ **hit rate**, $\text{AMAT}=1+(0.01*100)=2\text{ cycles}$.
Improving the **hit rate** by just $2\%$ resulted in double the average **memory speed**.

To avoid the large **miss penalty** we have multiple **caches**, more gradually bridging the **gap** between **L1 cache** and **main memory**.
* L1 **cache** is incredibly **fast**, taking $4$ **cycles**, but it **misses** $3\text{-}10\%$ of the time because it is so small.
* L2 **cache** is slower, taking about $10$ **cycles** but is much **larger**, keeping the **miss** **rate** under $1\%$, and avoiding the $\approx 100\text{ cycle}$ **miss penalty**.

A **cache's** organisation is defined by the **tuple** $(S,N,B,m)$:
* $m$ is the number of [[Binary|bits]] in a **memory address**.
* $S$ is the number of **sets** the **cache** is divided into.
	* Note that $S$ is always a power of $2$.
* $N$ is the number of **cache lines** within each **set**.
* $B$ is the **block size**, the number of **bytes** stored within each **cache line**.
	* These are **adjacent bytes**, to take advantage of **spatial locality**.
The total **cache size** $C$ is given by $C=S\times N\times B$.
* The number of **blocks** is given by $\frac C B$, or $S\times N$.

To check the **cache** quickly, a **hash table** is used.
* Each **memory address** maps to a specific **cache** **address** using modulo arithmetic - `(block address) mod (number of blocks)`.
However, **main memory** is much larger than **cache**, so **collisions** are **inevitable**.
* The **CPU** therefore needs some way to identify if the **data** at the given **cache address** is the **data** its looking for or not.
Each $m$-**bit** address can be split into three fields:
* ![[Pasted image 20260420175036.png|302]]
* The middle $s$ **bits** are known as the **index**, and indicate the **set**.
	* The middle **bits** are used, to prevent **contiguous addresses** from **colliding**.
* The top $t$ bits are stored alongside the **block**, and are known as the **tag**.
	* During a lookup, the **CPU** compares the **tag** to the **tag** of the requested **data**.
* The bottom $b$ **bits** are known as the offset, and indicate the specific starting **byte** within the **block**.


> [!Note]
> A **cache line** only holds a single **block** of **data**, but it also holds other information such as the **tag**, or **control bits**.

> [!Note]
> In our case, we have so far looked at **direct-mapped cache**, where each **set** only contains a single **cache line**, i.e. $N=1$.