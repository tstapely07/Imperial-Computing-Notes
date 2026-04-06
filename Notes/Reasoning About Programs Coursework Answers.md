# Question 1
## a.
Given:
$R(0)=1$
$R(n)=2*R(n-1)+(n-1)-1$

To show:
$\forall n: \mathbb{N}.[R(n)=2^n-n]$

Proof:
Base case:
To show: $R(0)=2^0-0$
$LHS=R(0)$
$=1$ - by definition of $R$
$=1-0$ - by arithmetic
$=2^0-0$ - by arithmetic
$=RHS$.
Hence base case holds.

Inductive step:
Take arbitrary $k\in\mathbb{N}$
Inductive hypothesis: Assume $R(k)=2^k-k$
To show: $R(k+1)=2^{k+1}-(k+1)$
$LHS=2*R(k)+(k+1-1)-1$ - by recursive definition of $R$
$=2*(2^k-k)+(k+1-1)-1$ - by inductive hypothesis
$=2*2^k-2k+(k+1-1)-1$ - by expanding brackets
$=2*2^k-k-1$ - by arithmetic
$=2^{k+1}-(k+1)$ - by arithmetic
$=RHS$
Hence inductive step holds if inductive hypothesis holds.

Therefore, by the principle of Mathematical Induction, $\forall n:\mathbb{N}.[R(n)=2^n-n]$ holds.
## b.
$R(52)=4.5\times10^{15}$

## c.
#### i.
Inductive principle: 
$(P([])\land \forall c:Card.\forall k:Hand.[P(k)\to P(c:k)]) \to \forall h:Hand.P(h)$
#### ii.
Inductive principle: 
$(P([])\land \forall c:Card.\forall k:Hand.[P(k)\to P(c:k)]) \to \forall d:Deck.P(d)$
#### iii.
Inductive principle: 
$$(\begin{gather}(\forall i:Int.R(Start\;i))\\
\land (\forall i:Int, d:Deck, h:Hand, g:History.[R(g)\to R(Turn\;i\;d\;h\;g)]))\\
\to \forall g:History.R(g)
\end{gather}$$
## d.
Given:
Definitions of $lose$, $bust$, $handvalue$, $cardvalue$, $draw$, and $Turn$
Lemmas CardRng, CardVal, and HandVal
To show:
$$\begin{align}&\forall d:Deck,s:Suit,h:Hand,i:Int,p:History\\
&d\neq[]\land(A,s)\in h\land\neg(lose\;(Turn\;i\;d\;h\;p)\;Hi)\to\neg(lose\;(draw\;(Turn\;i\;d\;h\;p))\;Lo)\end{align}$$
We first prove the Lemma HandHiLo:
To show: $\forall h:Hand.[handvalue\;h\;Hi \geq handvalue\;h\;Lo]$
The proof is by structural induction over $h$.
Base case:
To show:
$handvalue\;[]\;Hi\geq handvalue\;[]\;Lo$
$LHS=handvalue\;[]\;Hi$
$=0$ - by definition of $handvalue$
$RHS=handvalue\;[]\;Lo$
$=0$ - by definition of $handvalue$
$LHS=0=RHS$ so $LHS\geq RHS$ 
So base case holds.

Inductive step:
Take arbitrary $c:Card$,$cs:Hand$
Inductive hypothesis: Assume $handvalue\;cs\;Hi\geq handvalue\;cs\;Lo$
To show:
$handvalue\;(c:cs)\;Hi\geq handvalue\;(c:cs)\;Lo$
$LHS=handvalue\;(c:cs)\;Hi$
=$cardvalue\;c\;Hi+handvalue\;cs\;Hi$ - by definition of $handvalue$
$\geq cardvalue\;c\;Lo+handvalue\;cs\;Hi$ - by Lemma CardVal
$\geq cardvalue\;c\;Lo+handvalue\;cs\;Lo$ - by induction hypothesis
$=handvalue\;(c:cs)\;Lo$ - by definition of $handvalue$.
So the inductive step holds if the inductive hypothesis holds.

Therefore by structural induction, the Lemma HandHiLo holds for all hands.


Now we prove the Lemma AceDiff.
To show:
$\forall h:Hand,s:Suit.[(A,s)\in h\to (handvalue\;h\;Hi\geq handvalue\;h\;Lo+10)]$
Proof:
Take arbitrary $h:Hand,s:Suit$
Assume $(A,s)\in h$.
$LHS=handvalue\;h\;Hi$
$=handvalue\;((A,s):(h\textbackslash\textbackslash[(A,s)]))\;Hi$ - by Lemma HandVal, since $(A,s)\in h$
$=cardvalue\;(A,s)\;Hi+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Hi$  - by definition of $handvalue$
$=11+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Hi$ - by definition of $cardvalue$
$\geq 11+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Lo$ - by Lemma HandHiLo
$=10+1+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Lo$ - by arithmetic
$=10+fromEnum\;A+1+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Lo$ - by definition of $fromEnum$, since $A$ is first in $Value$ 
$=10+cardvalue\;(A,s)\;Lo+handvalue\;(h\textbackslash\textbackslash[(A,s)])\;Lo$ - by definition of $cardvalue$
$=10+handvalue\;((A,s):(h\textbackslash\textbackslash[(A,s)]))\;Lo$ - by definition of $handvalue$
$=RHS$

So $LHS\geq RHS$ so Lemma AceDiff holds.

Now the main proof can be carried out.
To show:
($\alpha$)$$\begin{align}&\forall d:Deck,s:Suit,h:Hand,i:Int,p:History\\
&d\neq[]\land(A,s)\in h\land\neg(lose\;(Turn\;i\;d\;h\;p)\;Hi)\to\neg(lose\;(draw\;(Turn\;i\;d\;h\;p))\;Lo)\end{align}$$
Proof:
Take arbitrary $d,s,h,i,p$.
(ass1) $d\neq []$
(ass2) $(A,s)\in h$
(ass3) $\neg(lose\;(Turn\;i\;d\;h\;p)\;Hi)$
(1) $\neg(bust\;h\;Hi)$ - from (ass3) and definition of $lose$.
(2) $\neg(handvalue\;h\;Hi\gt 21)$ - from (1) and definition of $bust$
(3) $handvalue\;h\;Hi\leq21$ - from (2) and negation of inequality
(4) $handvalue\;h\;Hi\geq handvalue\;h\;Lo+10$ - from (ass2) and Lemma AceDiff
(5) $handvalue\;h\;Lo + 10 \leq 21$ - from (3) and (4)
(6) $handvalue\;h\;Lo \leq 11$ - from (5) and arithmetic
(7) $\exists c,ds.[d=c:ds]$ - from (ass1) and definition of lists.
(8) Let $p'=Turn\;i\;(c:ds)\;h\;p$ - new variable to represent $newpast$.
(9) $draw\;(Turn\;i\;d\;h\;p)=Turn\;(i+1)\;ds\;(c:h)\;p'$ - from (7), (8), and definition of $draw$.
(10) $handvalue\;(c:h)\;Lo=cardvalue\;c\;Lo+handvalue\;h\;Lo$ - from definition of $handvalue$
(11) $cardvalue\;c\;Lo\leq 10$ - from Lemma CardRng
(12) $handvalue\;(c:h)\;Lo\leq 10 +11$ - from substituting (6), (11) into (10)
(13) $handvalue\;(c:h)\;Lo\leq 21$ - from arithmetic
(14) $\neg(handvalue\;(c:h)\;Lo\gt 21)$ - from (13) and negation of inequality
(15) $\neg(bust\;(c:h)\;Lo)$ - from (14) and definition of $bust$
(16) $\neg(lose\;(Turn\;(i+1)\;ds\;(c:h)\;p')\;Lo)$ - from (15) and definition of $lose$
(17) $\neg(lose\;(draw\;(Turn\;i\;d\;h\;p))\;Lo)$ - from (16) and (9)

Line (17) matches the consequent of $\alpha$, which we reached by assuming the $antecedent$.
Therefore the property $\alpha$ has been shown.

## e.
#### i.
We aim to prove $\forall x,y .[Odd(x)\land Odd(y)\to Even(add(x,y))]$.
Using the standard logical equivalence $A\land B\to C \equiv A\to(B\to C)$, we can rewrite this as $\forall x.[Odd(x)\to(\forall y.[Odd(y)\to Even(add(x,y))])]$.

Let $P(x)$ be the property: $\forall y\in S_{\mathbb{N}}.[Odd(y)\to Even(add(x,y))]$
Inductive principle:
$$\begin{gather}
(P(Succ(Zero))\\
\land \forall k\in S_\mathbb{N}.[Odd(k)\land P(k)\to P(Succ(Succ(k)))])\\
\to \forall x\in S_{\mathbb{N}}.[Odd(x)\to P(x)]
\end{gather}$$
Written out in full, this inductive principle is:
$$\begin{gather}
(\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(Succ(Zero), y))])\\
\land (\forall k \in S_\mathbb{N}.[Odd(k)\land (\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(k,y))])\\
\to(\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(Succ(Succ(k)),y))])])\\
\to \forall x\in S_\mathbb{N}.[Odd(x)\to(\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(x,y))])]
\end{gather}$$
#### ii.
Base case:
To show: $\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(Succ(Zero), y))]$
Take arbitrary $y\in S_\mathbb{N}$
(ass1) $Odd(y)$
(1) $add(Succ(Zero),y)=Succ(add(Zero,y))$ - by definition of $add$
(2) $add(Zero,y)=y$ - by definition of $add$ 
(3) $add(Succ(Zero),y)=Succ(y)$ - by substituting (2) into (1)
(4) $Even(Succ(y))$ - by Lemma OddSucc and (ass1)
(5) $Even(add(Succ(Zero),y))$ - by substituting (3) into (4)
We have reached the consequent by assuming the antecedent, so the base case holds.

Inductive step:
Take arbitrary $k\in S_\mathbb{N}$
Inductive hypothesis: Assume $\forall y\in S_\mathbb{N}.[Odd(y)\to Even(add(k,y))]$
To show:
$\forall y \in S_\mathbb{N}.[Odd(y)\to Even(add(Succ(Succ(k)),y))]$
Proof:
Take arbitrary $y\in S_\mathbb{N}$.
ass(1) $Odd(y)$
(1) $add(Succ(Succ(k)),y)=Succ(add(Succ(k),y))$ - by definition of $add$
(2) $add(Succ(k),y)=Succ(add(k,y))$ - by definition of $add$
(3) $add(Succ(Succ(k)),y)=Succ(Succ(add(k,y)))$ - by substituting (2) into (1)
(4) $Even(add(k,y))$ - from (ass1) and IH
(5) $Even(Succ(Succ(add(k,y))))$ - from R6 and (4)
(6) $Even(add(Succ(Succ(k)),y))$ - by substituting (3) into (5)
We have reached the desired result by assuming the inductive hypothesis, so the inductive step holds.

Since both the base case and the inductive step holds, the property $\forall x, y\in S_{\mathbb{N}}.[Odd(x)\land Odd(y)\to Even(add(x,y))]$ has been proven by induction over the definition of $Odd$.

## f.
The inductive principle is:
$$\begin{gather}
(
(\forall l,k,b,t.[l\geq 2k \to Ideal(l,k,b,t,10(b+t))])\\
\land (\forall l,k,b,t.[l\lt 2k \land k+b=t \to Ideal(l,k,b,t,5*(l-1))])\\
\land (\forall l,k,b,t.[l\lt 2k \land k+b\neq t \land Ideal(l,k,b-1,t-1,ratehouse(l,k,b-1,t-1))\\\to Ideal(l,k,b,t,2+ratehouse(l,k,b-1,t-1))])
)\\
\to\\
\forall l,k,b,t,v.[ratehouse(l,k,b,t)=v\to Ideal(l,k,b,t,v)]
\end{gather}$$

