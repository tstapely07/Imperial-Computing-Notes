# Question 1
## a.
```Haskell
enc (Node (Leaf 3) (Node (Leaf 5) (Leaf 7))) 
= (Nd : enc (Leaf 3)) ++ enc (Node (Leaf 5) (Leaf 7)) 
= (Nd : [Lf 3]) ++ ((Nd : enc (Leaf 5)) ++ enc (Leaf 7)) 
= [Nd, Lf 3] ++ ((Nd : [Lf 5]) ++ [Lf 7]) 
= [Nd, Lf 3] ++ ([Nd, Lf 5] ++ [Lf 7]) 
= [Nd, Lf 3] ++ [Nd, Lf 5, Lf 7] 
= [Nd, Lf 3, Nd, Lf 5, Lf 7]
```
## b.
```Haskell
enc (Node (Node (Leaf 3) (Leaf 5)) (Leaf 7)) 
= (Nd : enc (Node (Leaf 3) (Leaf 5))) ++ enc (Leaf 7) 
= (Nd : ((Nd : enc (Leaf 3)) ++ enc (Leaf 5))) ++ [Lf 7] 
= (Nd : ((Nd : [Lf 3]) ++ [Lf 5])) ++ [Lf 7] 
= (Nd : ([Nd, Lf 3] ++ [Lf 5])) ++ [Lf 7] 
= (Nd : [Nd, Lf 3, Lf 5]) ++ [Lf 7] 
= [Nd, Nd, Lf 3, Lf 5] ++ [Lf 7] 
= [Nd, Nd, Lf 3, Lf 5, Lf 7]
```

# Question 2
Let $P(t)$ be the property: $length(enc, t)=size\,t$ 
To prove $\forall t:Tree.P(t)$, we must show:
* Base case: $\forall i:Int.P(Leaf\,i)$
* Inductive step: $\forall t1, t2 : Tree. (P(t1) \land P(t2) \implies P(Node\, t1 \ t2))$

Base case:
To show $\forall i:Int.length(enc(Leaf\,i))=size(Leaf\, i)$
Take arbitrary integer $i$.
LHS:
$length(enc(Leaf\,i))$
$=length[Lf\,i]$ - by definition of $enc$.
$=length(Lf\,i: [])$ - by lemma C.
$=1+length\,[]$ - by definition of $length$
=$1+0$ - by definition of $length$
$=1$ - by arithmetic.
$=size(Leaf\;i)$ - by definition of $size$
$=RHS$

Inductive step:
Take arbitrary trees $t1$, $t2$.
Assume $length(enc\,t1)=size\,t1$ and $length(enc\,t2)=size\,t2$
To show $length(enc(Node\,t1\,t2))=size(Node\,t1\,t2)$
Starting from LHS:
$length(enc(Node\,t1\,t2))$
$=length((Nd:(enc\,t1))++ (enc\,t2))$ - by definition of $enc$
= $length(Nd:(enc\,t1))+length(enc\,t2)$ - by lemma A.
$=(1+length(enc\,t1))+length(enc\,t2)$ - by definition of $length$.
$=1+size\,t1+size\,t2$ - by induction hypothesis.
$=size(Node\,t1\,t2)$ - by definition of $size$.
$=RHS$
So $P(Node\,t1\,t2)$ holds.

By the principle of structural induction, we conclude that $\forall t:Tree.length(enc\;t)=size\;t$. 


# Question 3
## a.
```Haskell
decAux [(Lf 3), Nd, (Lf 5), (Lf 7)]
= (Leaf 3,[Nd,Lf 5,Lf 7])
```
## b.
```Haskell
decAux [Nd,(Lf 3),(Lf 5),(Lf 7)]
= (Node (Leaf 3) (Leaf 5),[Lf 7])
```
## c.
```Haskell
dec [(Lf 3),Nd,(Lf 5),(Lf 7)]
= undefined -- since the [Nd,lf 5, lf 7] returned from decAux won't match the []
```
## d.
```Haskell
dec [Nd,(Lf 3),(Lf 5)]
= Node (Leaf 3) (Leaf 5)
```

## Question 4
Let $P(t)$ be the property $\forall cds: [Code].decAux((enc\;t)++cds)=(t,cds)$
We must show:
* Base case: $\forall i:Int.P(Leaf\;i)$
* Inductive step: $\forall t1, t2:Tree.P(t1)\land P(t2)\implies P(Node\;t1\;t2)$

Base case:
To show $\forall i:Int.\forall cds:[Code].decAux((enc(Leaf\;i))++cds)=(Leaf\;i, cds)$
Take arbitrary integer $i$ and arbitrary list $cds$.
$LHS=decAux((enc(Leaf\;i))++cds)$
$=decAux([Lf\;i]++cds)$ - by definition of $enc$.
$=decAux(Lf \;i:cds)$ - by lemma E.
$=(Leaf\;i,cds)$ - by definition of $decAux$.
$=RHS$.
So property holds for the base case.

Inductive step:
Take arbitrary trees. $t1$, $t2$.
Assume $\forall cds.decAux((enc\;t1)++cds)=(t1, cds)$ and $\forall cds.decAux((enc\;t2)++cds)=(t2, cds)$.

To show $\forall cds.decAux((Node\;t1\;t2)++cds)=(Node\;t1\;t2,cds)$
Take an arbitrary list $cds$.
$LHS=decAux((enc(Node\;t1\;t2))++cds)$
$=decAux(((Nd:enc\;t1)++enc\;t2)++cds)$ - by definition of $enc$.
$=decAux((Nd:enc\;t1)++(enc\;t2++cds))$ - by lemma D.
$=decAux(Nd:(enc\;t1++(enc\;t2++cds)))$ - by lemma $B$.
First call:
$(t1, cds1) = decAux(enc\;t1++(enc\;t2++cds)$
$(t1,cds1)=(t1, (enc\;t2++cds)$ - by induction hypothesis.
Second recursive call:
$(t2, cds2)=decAux(enc\;t2++cds)$
$(t2, cds2)=(t2, cds)$ - by induction hypothesis.
So $LHS=(decAux(Node\;t1\;t2), cds)$ - by definition of $decAux$
$=RHS$.
So property holds for the inductive step.

By the principle of structural induction, we conclude that $\forall t:Tree.\forall cds:[Code].decAux((enc\;t)++cds)=(t, cds)$

## Question 5
## a.
```Haskell
encd (Node (Leaf 3) (Node (Leaf 5) (Leaf 7)))
= [Lf 3,Lf 5,Lf 7,Nd,Nd]
```
## b.
```Haskell
encd (Node (Node (Leaf 3) (Leaf 5)) (Leaf 7))
= [Lf 3,Lf 5,Nd,Lf 7,Nd]
```
## c.
```Haskell
decdAux [(Lf 9)] [(Node (Leaf 5) (Leaf 7)),(Leaf 3)]
= Leaf 9
```
## d.
```Haskell
decdAux [(Lf 5),(Lf 7),Nd,(Lf 9)] [(Leaf 3)]
= Leaf 9
```

# Question 6
Stronger assertion (vii):
$$\forall t:Tree\;\forall cds:[Code]\;\forall ts:[Tree].decdAux((encd(t)++cds)\;ts=decdAux\;cds\;(t:ts)$$
We can show how (vii) implies (vi) by initialising (vii) with specific values:
* Let $cds=[]$
* Let $ts=[]$.
We now get:
$\forall t:Tree.decdAux((encd\;t)++[])\;[]=decdAux\;[]\;(t:[])$
$=\forall t:Tree.decdAux(encd\;t)\;[]=decdAux\;[]\;(t:[])$ - by identity of list concatenation.
$=\forall t:Tree.decdAux(encd\;t)\;[]=t$ - by definition of $decdAux$.
This matches assertion (vi) exactly, so (vii) is just a more general case of (vi), and therefore (vii) does indeed imply (vi).

# Question 7
To prove $\forall m:Map\;a\;b.P(m)$.
Induction principle:
$$\begin{align}
&(P(None)\\
&\land \forall x:a.P(Last\;x)\\
&\land \forall y:b.\forall m:Map\;a\;b.(P(m)\implies P(Comb\;y\;m)))\\
&\implies \forall m:Map\;a\;b.P(m)
\end{align}$$



