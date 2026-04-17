---
date: 2026-04-17
tags:
  - first-year
  - M40005
---
When designing a **control unit** for our [[RISC-V Architecture|RISC-V]] [[multi-cycle datapath]], we ended up with this [[State Transition Tables|state transition diagram]], illustrating the **control signals** at each **state**:
* ![[Pasted image 20260417102352.png|470]]

One way to improve this is by using **abstraction**, specifically **field assignments**.
* Instead of writing `ALUSrcA=1` or `ALUOp=10`, we replace these by readable values that indicate what the [[binary]] means, such as `ALuSrcA=A` or `ALUOp = funct`.
We can also use a single **field assignment** to handle multiple control signals:
* `RegWrite=1` and `MemtoReg=0` are both set at the same time in state $7$, so let's group them to `RegCtrl=WriteMDR`.
* Again, this higher level of **abstraction** better captures the **semantics** of the **operation**.

Overall, we can group the $13$ **control signals** (which span $15$ **bits**) into just $7$ **fields**, each covering multiple related **signals**.
* We divide these $7$ **fields** into two **logical groups**, the **ALU** related **fields** and the **read/write/sequencing** **fields**.
The **ALU** related **fields**:
* ![[Pasted image 20260417103248.png|384]]
The **read/write** related **fields**:
* ![[Pasted image 20260417103355.png|383]]
The **state transition diagram** is more manageable now:
* ![[Pasted image 20260417103442.png|442]]

Previously, we used a [[Finite State Machines|finite state machine]] to handle the **state sequencing logic**.
* However, since our **transitions** are very structured, that ends up being a waste of **silicon space**.

There are $4$ possible ways that the **next** **state** might be determined:
1. Simply stepping through the **states** in order, i.e. `next = current + 1`
2. Using the `opcode` to determine the next **state**.
3. Returning to state $0$ when an **instruction** is finished.
4. A hardcoded jump, for example, **R-type instructions** always jump from **state** $2$ to **state** $4$.
We can represent these by the following **values** for the `sequencing` **field**:
* ![[Pasted image 20260417105442.png|510]]
* `seq` corresponds to possibility $1$, `fetch` to possibility $3$, `dispatch1`/`dispatch2` to possibility $2$, and `R/I-wb` to possibility $4$.
We can now compress our **state transition diagram** into a single **table**, showing what **fields** must be set at each **state**, including the **sequencing**:
* ![[Pasted image 20260417105807.png|492]]
* The red arrows indicate how the **sequencing** column is used by a `ld` instruction, by tracing the **states**.
* The value in the **sequencing** column indicates how the **next** **state** should be determined.

We can implement this using a **microsequencer**:
* ![[Pasted image 20260417110337.png|511]]
* Here, $\micro PC$ is a $4$-**bit** [[Registers|register]] to store the current **state**.
* The $5$ **inputs** to the [[Multiplexers|multiplexer]] indicate the different possibilities for the next state (`DR1` and `DR2` implement `dispatch1` and `dispatch2`).
* The **address control input** determines which **input** should be chosen as the **output** as follows:
	* $000$ - `fetch` - constant $0$.
	* $001$ - `R/I-wb` - constant $4$.
	* $010$  - `dr1` - **dispatch ROM** $1$.
	* $011$  - `dr2` - **dispatch ROM** $2$.
	* $100$ - `seq` - increment **state**.
* The [[Combinatorial Circuits|combinational]] **control logic** implements the **state table**, by mapping the $\micro PC$ value into the $15$ **bits** of **control signals**, as well as the **address control signals**, equivalent to the `sequencing` column, which are passed to the **multiplexer**.
`dispatch1` and `dispatch2` are implemented using **ROM** that stores their **truth tables**, as follows:
* ![[Pasted image 20260417110958.png|603]]
* ![[Pasted image 20260417111033.png|386]]

But what is the benefit of this approach, over our previous **ROM** based approach.
Previously, the **ROM** had $11$ **bits** of **input**, and had to generate **19** **output** **bits**.
* This means a **total size** of $2^{11}\times 19=38912$ **bits**.
Now our **ROMS** are smaller, even though we now have $3$.
* Their total size is $2^4\times 18 + 2(2^7\times 4)=1312$ **bits**.
This is a significant decrease, even when we include the addition of the $\micro PC$ **register** and a **multiplexer**.

This **microsequencer** implemented **horizontal microcoding**.
* There is also **vertical** **microcoding**, where we use fewer **bits** in the **combinational logic** than we have **control signals**.
* We then use an additional [[Decoders|decoder]].
For example, we only need $2$ **bits** to represent these $3$ **control signals**, since some combinations will never occur:
* ![[Pasted image 20260417113753.png|488]]

**Vertical** and **horizontal** **microcoding** both have **pros** and **cons**.
**Horizontal**:
* **Pros**:
	* Every component has its own **multiplexer**, so we can execute multiple operations at the same time.
	* The signals go straight from the **ROM** to the **datapath**, with no delay from additional [[logic gates]].
* **Cons**:
	* Requires a wider, larger **ROM** chip.
**Vertical**:
* **Pros**:
	* Takes up less **ROM** space.
	* Only handling one operation at a time means **microcode** is easier for humans to write.
* **Cons**:
	* Slower execution, since we must execute operations sequentially.
	* The **decoder** can add a delay.
We should generally only **encode** the **non-time-critical parts**.

