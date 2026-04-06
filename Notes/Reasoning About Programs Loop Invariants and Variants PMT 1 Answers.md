# Question 1
## a.
$$M\triangleq \neg stop\leftrightarrow Palindrome(s[..))$$
## b.
$$I\triangleq 0\le i\le s.length/2\;\land\;(\neg stop\leftrightarrow PartPalin(s[..),i))$$
## c.
$$V=s.length/2-i$$
This variant decreases because $i$ is incremented by $1$ every iteration.
It is bounded below by $0$ since the loop condition $i\lt s.length / 2$ prevents $i$ from ever exceeding $s.length / 2$.

# Question 2
## a.
$$M\triangleq (found \land i-j=First(s[..), t[..)))\lor(\neg found \land s.length=First(s[..), t[..))$$
## b.
$$\begin{gather}I\triangleq 0\le i\le s.length\land 0\le j\le t.length\land j\le i\\
\land \forall k\in[0..i-j).[\neg Matched(s[..),t[..),k)]\\
\land PartMatch(s[..),t[..),i-j,j)\\
found\leftrightarrow j=t.length\end{gather}$$
## c.
$$V=(s.length-(i-j),t.length-j)$$
We can justify that this decreases every iteration by considering both the then and else branches of the if statement.
In the if branch, both $i$ and $j$ are incremented. This means that $(i-j)$ is unchanged, and so the first element of the tuple remains the same. However, because $j$ increases, $t.length-j$ strictly decreases, so the tuple lexicographically decreases.
In the else branch, $i$ becomes $i-j+1$, and $j$ becomes $0$. So now the new value of $(i-j)$ is $i-j+1-0=i-j+1$. So since $(i-j)$ is incremented by 1, the first element $s.length-(i-j)$ strictly decreases, and so the tuple lexicographically decreases.

The tuple is bounded below by $(0,0)$. The invariant states that $j\ge 0$, so clearly $i-j\le i$. Since $i$ can never exceed $s.length$, as enforced by the loop condition, $i-j$ can never exceed $s.length$, so $s.length-(i-j)$ is bounded below by $0$. 
The loop condition enforces $j<t.length$. This means $j$ can never exceed $t.length$ and so $t.length-j$ is strictly bounded below by 0.