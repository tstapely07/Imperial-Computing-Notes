---
date: 2026-04-12
tags:
  - first-year
  - M40001
---
If we combine our $8$-[[Binary|bit]] [[manual processor]] from before with the [[Connecting RAM to a Processor|memory]] we designed, we end up with this:
* ![[Pasted image 20260412124239.png|341]]
However, this arrangement has many issues:
* [[The Fetch Cycle|Fetching]] **data** from **memory** requires three additional **states**. 
* There are $4$ different inputs we require from memory, so we now have $4\times 3+5=17$ **states** required.
* We also need more states to get the address into the **MAR** when we write to memory.
* Overall, this design ends up being extremely slow.

We can make some improvements:
* We can change all [[System Buses|buses]] from $8$ **bits** to $32$ **bits**, so we can do $4$ times as much work in each [[Clocks|clock cycle]].
* We can provide **local** [[registers]] to store partial results.
* We can redesign our **controller** [[Sequential Circuits|circuit]] to ensure the minimum amount of execution **cycles**.
* We can avoid the need for elaborate carry arrangements, but doing all our [[Signed Binary Arithmetic|arithmetic]] directly on big integers.
* We can replace the bi-directional **data bus** with separate **data-in** and **data-out** buses for the **memory**.
Now our processor looks like this:
* ![[Pasted image 20260412135611.png|590]]
* Since most **arithmetic operations** will no longer require a carry in, rather than our complex carry logic from before, we can simply set $C_{in}$ directly from the **controller**.

We must now design the **controller**.
We know that each **fetch cycle** retrieves one $32$-**bit** instruction from memory, so to design a **controller** we must first define the **instruction format**.
**Instructions** that reference **memory** directly take the following form:
* ![[Pasted image 20260412140049.png]]
The **instructions** of this form are:
* `LOAD Reg, Address`
* `STORE Reg, Address`
* `JUMP Address`
* `CALL Reg, Address`
For these **instructions**, since we only identify **addresses** using $20$ **bits**, and our addresses are $32$ **bit** numbers, we need a **bit mask**, like this:
* ![[Pasted image 20260412140304.png|236]]

To allow us to **address** the entire range of **memory addresses**, we also use **indirect addressing**, where a $32$-**bit** address is stored in a **register.**
These **instructions** take the following form:
* ![[Pasted image 20260412142114.png|321]] 
The **instructions** themselves are:
* `LOADINDIRECT Reg1, Reg2`
* `STOREINDIRECT Reg1, Reg2`
* `JUMPINDIRECT Reg`
* `CALLINDIRECT Reg1, Reg2`

We also have **instructions** that work with two internal **registers**. 
These take the same form as the **indirect addressing instructions**
* ![[Pasted image 20260412142114.png|321]] 
The **instructions** themselves are:
* `MOV Rdest, Rscr`
* `ADD Rdest, Rscr`
* `SUBTRACT Rdest, Rscr`
* `AND Rdest, Rscr`
* `OR Rdest, Rscr`
* `XOR Rdest, Rscr`
* `COMPARE Rdest, Rscr` - like `SUBTRACT` but without storing the result.

Some **instructions** only take a single internal register, and have this form:
* ![[Pasted image 20260412180107.png|341]]
These are:
* `CLEAR Rdest`
* `INC Rdest` - increment.
* `DEC Rdest` - decrement.
* `COMP Rdest` - complement.
* `ASL Rdest` - arithmetic shift left.
* `ASR Rdest` - arithmetic shift right.
* `ROR Rdest` - rotate right.
* `RETURN Rdest`

Finally, some **instructions** take no **register** arguments, and so have this form:
* ![[Pasted image 20260412180403.png]]
These are:
* `SKIPPOSITIVE`
* `SKIPNEGATIVE`
* `SKIP` - unconditional.
* `NOP` - no instruction, used when an instruction is expected but no work needs doing.

**Input** and **output** can be handled using `LOAD` and `STORE`.
* We can often control **peripherals** by treating them as if we are writing to **memory**.

Now, each **instruction** requires a sequence of **register transfers** to carry them out.
The **register transfers** are always the same in the **fetch** stage, the three states are:
* $F_1:MAR\leftarrow PC;PC\leftarrow PC+1$
* $F_2:MDR\leftarrow Memory$
* $F_3: IR\leftarrow MDR$
In the **execute** stage, the **register transfers** differ, depending which **instruction** is being executed.
For the **memory reference instructions**:
* ![[Pasted image 20260412180910.png|441]]
For the **indirect memory reference instructions**:
* ![[Pasted image 20260412180930.png|443]]
For the **two register instructions**:
* ![[Pasted image 20260412180941.png|446]]
For the **one register instructions**
* ![[Pasted image 20260412180956.png|441]]
For the **no register instructions**:
* ![[Pasted image 20260412181034.png|443]]
* `SKIPPOSITIVE` and `SKIPNEGATIVE` also take one **cycle**, and may or may not increment the **program counter**, depending on the **carry**.
* The `NOP` instruction doesn't require any **cycles**, and has no **register transfers**.

Now we can design the **controller**.
* We need $3$ **fetch states**.
* The highest number of **cycles** needed by an **instruction** was $4$, so we therefore need $4$ **execute states**.
These **states** gives this [[Finite State Machines|finite state machine]]:
*  ![[Pasted image 20260413092928.png|281]]
We will need a [[Combinatorial Circuits|combinatorial circuit]], with a single **output**, $C$, to determine whether we should continue to the next execution state, or **fetch** the next **instruction**.  
* The **inputs** will be the **instruction op-code bits** and the **state**.
We can use an $8$ to $256$ **decoder** to **decode** the the **opcode** and determine the current instruction:
* ![[Pasted image 20260413093341.png|258]]
* We can also group instructions with the same **state sequence**: 
	* `ADDS=ADD+SUBTRACT+AND+OR+XOR`
	* `SHIFTS=ASL+ASR+ROR`
	* `SKIPS=SKIP+SKIPOSITIVE+SKIPNEGATIVE`
To give the **state input**, we must first choose how to represent the **state**.
* Since we have $7$ states, we will use three [[Edge-Triggered D-Type Flip-Flop|flip-flops]].
* ![[Pasted image 20260413094123.png|257]]
Now we can use another **decoder**:
* ![[Pasted image 20260413094142.png|239]]
With **decoders** for the **instruction** and **state**, determining $C$ is simply a case for determining [[Boolean Algebra|Boolean expressions]] for each case when the **FSM** must **fetch** a new **instruction**:
$$\begin{gather}C=(F3\cdot NOP)'\cdot\\ (E1\cdot (SKIPS+CLEAR+JUMP))'\cdot\\ (E2\cdot (REUTRN+SHIFTS+MOVE+JUMPINDIRECT))'\cdot\\ (E3\cdot (COMP+DEC+INC+COMPARE+\\ADDS+STOREINDIRECT+LOAD))'\end{gather}$$
* This can be implemented using [[logic gates]] directly.

Now we must design the **state sequencing logic**.
Our [[State Transition Tables|state transition table]] is simple to write out:
* ![[Pasted image 20260413094757.png|264]]
We then get the following [[Karnaugh maps]]:
* ![[Pasted image 20260413094827.png|293]]
To start with, we get the following **Boolean equations**:
* $D2=C\cdot Q2\cdot Q1'+C\cdot Q1\cdot Q0'$
* $D1=C\cdot Q1'+C\cdot Q2\cdot Q0'+Q2'\cdot Q1'\cdot Q0'$
* $D0=Q2'\cdot Q1'\cdot Q0'+Q2'\cdot Q1\cdot Q0+C\cdot Q2\cdot Q1\cdot Q0'$
Since we have already **decoded** the **states**, we can make a few simplifications, giving us the final **Boolean equations**:
*  $D2=C\cdot Q2\cdot Q1'+C\cdot Q1\cdot Q0'$
* $D1=C\cdot Q1+C\cdot Q2\cdot Q0+F1$
* $D0=F1+F2+C\cdot E3$
And now we have our final [[Sequential Circuits|circuit]]:
* ![[Pasted image 20260413100533.png|270]]

The **output logic** will take in the **state** and the **instruction bits** and needs to output **clock signals**, **function select lines** to the **ALU**, and **multiplexer select lines**.
This **circuit** will take the form of a [[Finite State Machines#^782dff|Mealy machine]], since the **output logic** will also depend on the **input**, as well as the current **state**.

We have **clock signals** $C0\to C14$ to ensure only certain **registers** are written to.
Each **clock signal** works by gating the **system clock**, like so:
* ![[Pasted image 20260413101847.png|270]]
We can then look at when we set the **MAR**, and get the equation:
$$\begin{gather}
CMAR=F1+\\E1\cdot (LOAD+STORE)+\\ E2\cdot (LOADINDIRECT+STOREINDIRECT)
\end{gather}$$
But in practice, the value of the **MAR** is only important when we are about to access **memory**.
* If we wrote to the **MAR** at other times, it wouldn't actually matter, so we can simplify our **equation**.
* $CMAR=F1+E1+E2$
We can repeat a similar design procedure for many of the other **register clocks**.
For example, for the **MDR**, we obtain:
* $CMDR=F2+E2\cdot LOAD+E3\cdot LOADINDIRECT$.
* Similar to before, we can notice that after $E3$, only `LOADINDIRECT` uses the `MAR`.
* We cannot get rid of the `LOAD` condition, since in $E3$ `CALL` reads the value in the **MDR** from $E2$, so we must not **overwrite** this.
* So we end up with $CMDR=F2+E2\cdot LOAD+E3$.
Since it is a similar methodology, the equations for the other **clocks** will be left off, for brevity.
* However, note that the clock for the **PC** depends on the **ALU carry-out**, since this is used in `SKIPPOSITIVE` and `SKIPNEGATIVE`.
The **clocks** for the individual **programmable registers** can be gated using a **decoder**, like in normal [[Register Transfer|register transfers]]:
* ![[Pasted image 20260413102537.png|264]]

Determining the **select bits** for the **shifter** is simple:
* ![[Pasted image 20260413103047.png|441]]
* $f4=ASR+ROR$
* $f3=ASL+ROR$
The **ALU** **select bits** can be determined in a similar fashion:
* ![[Pasted image 20260413103152.png|430]]
$$\begin{align}&f2=E3\cdot (COMP+OR+AND)+E2\cdot (COMP+DEC)\\
&f1=E3\cdot (SUBTRACT+COMPARE+DEC+INC+ADD+AND)+\\&\quad \quad \quad E2\cdot(COMP+DEC)\\
&f0=E3\cdot (DEC+INC+ADD+OR)+E2\cdot (COMP+DEC)\end{align}$$
The **ALU** **carry in** **bit** is only used by `INC`, in $E3$, so we can set:
* $f5=INC\cdot E3$

The final problem is determining the **multiplexer selection bits**.
The required **bit** selections are defined in this table:
* ![[Pasted image 20260413105026.png|472]]
Now we can look at when different paths should be selected, where $Spath$ means that $path$ should be selected:
* $SPC=E2\cdot (CALL+CALLINDIRECT)$
* $SALU=E1\cdot CLEAR+(E2+E3)\cdot (INC+DEC+COMP)+E3\cdot TWO$
	* Where $TWO$ is $1$ when a **two-register instruction** is executed.
	* So $TWO=MOV+ADD+SUBTRACT+AND+OR+XOR+COMPARE$
* $SMask=E1\cdot (LOAD+JUMP+STORE)+E3\cdot CALL$
* $SMDR=E3\cdot LOAD+E4$
Now we can define:
* $s4=SALU+SMDR$
* $s5=SPC$
* $s6=SMask+SMDR$
When selecting the **register**, we can often take $s2,s1,s0$ directly from the `Rsrc` or `Rdest` fields of the **instructions**.
* To determine whether we look at the `Rsrc` or `Rdest` **bits**, we can define $SRsrc$:
	* $SRsrc=E1\cdot (INDIRECT+TWO)$
* When executing a **one-register instruction**, we always want to load from the **bus**, and so set $s0,s1,s2=111$. For this, we define $SBus$:
	* $SBus=E2\cdot ONE$
	* Where $ONE=CLEAR+INC+DEC+COMP+ASL+ASR+ROR+RETURN$
Now we can define $s0,s1,s2$ with the following **circuit**, gated by $SRsrc$ and $SBus$:
* ![[Pasted image 20260413110356.png|377]]
Finally, we must define the **PC selector**.
* This should only **increment** with the following conditions:
* $s3=F1+E1\cdot (CALL+CALLINDIRECT)$
