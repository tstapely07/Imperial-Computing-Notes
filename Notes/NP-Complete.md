---
date: 2026-01-28
tags:
  - M40008
  - first-year
---
> [!Abstract] Definition
> A [[Decision Problems|decision problem]] $D$ is **NP-complete** (**NPC**) if:
> * $D\in NP$ 
> * $D$ is [[NP-hard]].

**NP-complete** **problems** are the **hardest problems** in [[Class NP|NP]].

While the definition doesn't guarantee that **NPC** **problems** exist, it has been shown that [[Satisfiability|SAT]] is **NP-complete**.

In general, to show a problem is **NPC**, it is easier to use [[reduction]], and show that:
* $D\in NP$ and $D'\le D$ for some known **NPC** problem $D'$. 
* Then, $D$ is also **NP-hard**, and therefore **NP-complete**.

Another **NPC problem** is the [[Hamiltonian Paths and Circuits|HamPath]] problem. 
* While the **reduction** is difficult, it can be shown that $SAT\le HamPath$. 


Let's prove that the [[Travelling Salesman Problem (TSP)|travelling salesman problem]] is **NP-complete**.
First we define a version of the **TSP** that is a **decision problem**:
We define $TSP(D)$ as: 
* Given a [[Weighted Graphs|weighted graph]] $(G,W)$ and a **bound** $B$, is there a **tour** of $G$ with **total weight** $\le B$?
We can show that $TSP(D)\in NP$ since, if we guess some **path** $\pi$,  we can check in **p-time** that $\pi$ is a [[Hamiltonian Paths and Circuits|Hamiltonian circuit]] of $G$, and that $W(\pi)\le B$.
* We clearly have $|\pi|\le|G|$ as required.
To show $D'\le TSP(D)$ for some **NPC problem** $D'$, we will show that $HamPath\le TSP(D)$.
We need to define a **p-time** function $f$ to transform $G$ into a **weighted graph** $G'$ and a **bound** $B$ such that $HamPath(G)\iff TSP(D)((G',W),B)$.
Given $G$, we can construct $(G',W)$ as follows:
* Set $nodes(G')=nodes(G)$.
* For any two distinct [[nodes]] $x,y$ of $G$:
	* If $(x,y)$ is an [[Arcs|arc]] of $G$, then $(x,y)$ is also an **arc** of $G'$, with $W(x,y)=1$.
	* If $(x,y)$ is not an [[Arcs|arc]] of $G$, then $(x,y)$ is an **arc** of $G'$, with $W(x,y)=2$.
* Finally, let $B=n+1$, where $G$ has $n$ **nodes**.
This function $f(G)=((G',W),B)$ is **p-time**.
We must now verify the $\iff$ condition.
Suppose $G$ has a **Hamiltonian path** $\pi$ with endpoints $x$ and $y$.
* The same **path** in $G'$ has **weight** $n-1$.
* We get a **travelling salesman tour** by adding in **arc** $(x,y)$ with $W(x,y)\le 2$, thus the **tour** has **weight** $\le n+1=B$.
Conversely, suppose $(G',W)$ has a **tour** of **weight** $\le B=n+1$.
* This has $n$ **arcs**, so at most $1$ **arc** can have **weight** $2$.
* Omitting this **arc** leaves us with a **Hamiltonian path** in $G$.
Since we have shown $HamPath\le TSP(D)$, and we know that $HamPath$ is **NP-hard**, we have shown that $TSP(D)$ is **NP-hard**.
We can therefore conclude that $TSP(D)$ is **NP-complete**.

Another **problem** is the **metric travelling salesman problem**, which is like the **standard travelling salesman problem**, but restricted to **graphs** that satisfy the [[Triangle Inequality (Calculus)|triangle inequality]].
Just like the standard **TSP**, we can easily prove that $MTSP(D)\in NP$:
* If we guess some **tour** $T$, we can verify in **p-time** if its weight is $\le B$ and if it visits every **node**.
Instead of trying to prove $TSP(D)\le MTSP(D)$, we can actually reuse the **reduction** from proving $HamPath\le TSP(D)$, since the **weighted graph** we designed already satisfies the **triangle inequality.**
* Therefore we have $HamPath \le MTSP(D)$, and therefore $MTSP(D)$ is **NP-hard**.
And so we can conclude that $MTSP(D)$ is **NP-complete**.

As a final example, lets consider show a **vehicle routing problem** to be **NP-complete**.
> [!Note] Vehicle Routing Problem VRPC(D)
> Given:
> * A [[Complete Graph|complete]] **weighted graph** $(G,W)$ satisfying the **triangle inequality**.
> * Some chosen $start$ **node**.
> * $k$ vehicles with capacity $C$.
> * A set of packages with sizes $s_1,\dots,s_n$ to be delivered to nodes $x_1,\dots,x_n$ respectively.
> * And a budget $B$.
> Can the packages be delivered within total cost $B$, subject to the total size of the packages of each vehicle being within the capacity $C$?

We can confirm that $VRPC(D)\in NP$, since we can check in **p-time** that:
* All packages are assigned to exactly one vehicle.
* The total size of packages does not exceed $C$ for each vehicle.
* The itinerary for each vehicle takes it from the depot, to each assigned delivery address, and back to the depot.
* The total cost does not exceed $B$.
To prove $VRPC(D)$ is **NP-hard**, we must **reduce** a known **NP-hard** problem to it.
* We choose **MTSP(D)**, due to the involvement of the **triangle inequality**.
Given a **metric graph** $(G,W)$ with $n$ **nodes** and a **bound** $B$, we define the our **vehicle routing problem** by:
* Keeping the **graph** the same, and using the **bound** $B$ as our **budget**.
* Picking any node to be the $start$ ndoe.
* Assign exactly $1$ package of size $1$ to every remaining **node**.
* Create exactly $1$ vehicle, with a capacity of $n-1$.
We must ensure that $MTSP(D)((G,W),B)\iff VRPC(D)(f((G,W),B))$.
First, suppose $MTSP(D)$ is true.
* Because we only have $1$ vehicle, which can hold all $n-1$ packages, the vehicle can just drive this exact **travelling salesman tour**, and the cost is $\le B$, so $VRPC(D)$ is satisfied.
Now suppose $VRPC(D)$ is true.
* This means the vehicle successfully visits all the **nodes**.
* However, the route may visit a **node** more than once, which is not allowed in the **travelling salesman problem**.
* Since the graph satisfies the **triangle inequality**, visiting a **node** twice is mathematically inefficient, and so we can simply avoid them.
* The **triangle inequality** guarantees the cost will never increase, so the **tour** is still $\le B$, and so $MTSP(D)$ is **satisfied**.
We have therefore shown that $VRPC(D)$ is **NP-hard**, and since it is in **NP**, it is **NP-complete**.