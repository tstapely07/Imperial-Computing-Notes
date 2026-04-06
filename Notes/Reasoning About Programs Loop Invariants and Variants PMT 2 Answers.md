# Question 1
Note that throughout this assignment, I will use the invariant, variant, and mid-condition provided, not my previous answers.
## a.
Proof obligation:
$$P\land var\;i=0\land var\;j=0\land var\;found=  (t.length==0)\to I$$
Given:
(1) $i=0$ (from code line 5)
(2) $j=0$ (from code line 6)
(3) $found \leftrightarrow (t.length=0)$ (from code line 7) 

To show:
($I_1$) $0\le i\le s.length\land 0\le j\le t.length \land i\ge j$
($I_2$) $PartMatch(s[..),t[..),i-j,j)$
($I_3$) $i-j\le First(s[..),t[..))$
($I_4$) $found\leftrightarrow j=t.length$

Proof:
(4) $0\le s.length$ (string length is non-negative)
(5) $0\le t.length$ (string length is non-negative)
(6) $0\le 0\le s.length \land 0\le 0\le t.length \land 0\ge 0$ (from (4), (5), and arithmetic)
$I_1$ follows from (6), (1), and (2)

(7)  $0\le k\le s.length\to PartMatch(s[..),t[..),m,0)$ (from Lemma 1)
(8) $0\le 0\le s.length\to PartMatch(s[..),t[..),0,0)$ (from instantiating (7) with $k=0$)
(9) $PartMatch(s[..),t[..),0,0)$ (from (4) and (8))
$I_2$ follows from (9), (1), and (2)

(10) $First(s[..), t[..)\ge 0$ (from Lemma 3)
(11) $0-0\le First(s[..),t[..))$ (from (10) and arithmetic)
$I_3$ follows from (11), (1), and (2)

(12) $(t.length=0)\leftrightarrow (0=t.length)$ (from symmetry of equality)
(13) $found\leftrightarrow (0=t.length)$ (from (3) and (12))
$I_4$ follows from (13) and (2)

## b.
Proof obligation:
$$\begin{gather}
I[i\mapsto i_{old},j\mapsto j_{old},found\mapsto found_{old}]\\
\land (j\lt t.length\land i\lt s.length \land \neg found)[i\mapsto i_{old},j\mapsto j_{old},found\mapsto found_{old}]\\
\land loop\_body\\
\to I
\end{gather}
$$
Universal givens:
(1) $0\le i_{old}\le s.length\land 0\le j_{old}\le t.length\land i_{old}\ge j_{old}$ (from I)
(2) $PartMatch(s[..),t[..),i_{old}-j_{old},j_{old})$ (from I)
(3) $i_{old}-j_{old}\le First(s[..),t[..))$ (from I)
(4) $found_{old}\leftrightarrow (j_{old}=t.length)$ (from I)
(5) $j_{old}\lt t.length$ (from cond)
(6) $i_{old}\le s.length$ (from cond)
(7) $\neg found_{old}$ (from cond)

To show:
($I_1$) $0\le i\le s.length\land 0\le j\le t.length \land i\ge j$
($I_2$) $PartMatch(s[..),t[..),i-j,j)$
($I_3$) $i-j\le First(s[..),t[..))$
($I_4$) $found\leftrightarrow j=t.length$

Case 1: 
Where $s[i_{old}]==t[j_{old}]$
Givens:
(8) $s[i_{old}]=t[j_{old}]$ (from if condition)
(9) $i=i_{old}+1$ (from code line 15)
(10) $j=j_{old}+1$ (from code line 16)
(11) $j=t.length\to found=true$ (from code line 17)
(12) $j\neq t.length\to found=found_{old}$ (from code line 17)

Proof:
(13) $i_{old}\lt s.length\to i_{old}+1\le  s.length$ (from (6) and arithmetic)
(14) $i\le s.length$ (from (13) and (9))
(15) $j_{old}\lt t.length\to j_{old}+1\le  t.length$ (from (5) and arithmetic)
(16) $j\le t.length$ (from (15) and (10))
(17) $i_{old}\ge j_{old}\to i_{old}+1\ge j_{old}+1$ (from (1) and arithmetic)
(18) $i\ge j$ (from (17), (9), and (10))
(19) $i_{old} \ge 0\to i_{old}+1\ge 1$ (from (1) and arithmetic)
(20) $i\ge 0$ (from (19) and (9))
(21) $j_{old} \ge 0\to j_{old}+1\ge 1$ (from (1) and arithmetic)
(22) $j\ge 0$ (from (21) and (10))
$I_1$ follows from (14), (16), (18), (20), (22)

(23) $i-j=(i_{old}+1)-(j_{old}+1)=i_{old}-j_{old}$ (from (9), (10), and arithmetic)
(24) $s[i_{old}-j_{old}..i_{old})\approx t[..j_{old})$ (from (2), definition of $PartMatch$ and arithmetic)
(25) $s[i_{old}-j_{old}..i_{old}+1)\approx t[..j_{old}+1)$ (from (24), (8), and properties of string concatenation)
(26) $PartMatch(s[..),t[..),i_{old}-j_{old},j_{old}+1)$ (from (25) and definition of $PartMatch$)
$I_2$ follows from substituting (23) and (10) into (26)

$I_3$ follows from (23) and (3)

(27) $j\neq t.length\to\neg found$ (from (7) and (12))
(28) $found \to j=t.length$ (from contrapositive of (27))
(29) $j=t.length\to found$ (from 11)
(30) $found\leftrightarrow j=t.length$ (from (28) and (29))
$I_4$ follows directly from (30)

(Note numbers 31 and 32 got cut out, and it would have taken too long to adjust the rest of the numbering, apologies.)

Case 2:
Where $s[i_{old}]\neq t[j_{old}]$
Givens:
(33) $s[i_{old}]\neq t[j_{old}]$ (from else condition)
(34) $i=i_{old}-j_{old}+1$ (from code line 19)
(35) $j=0$ (from code line 20)
(36) $found=found_{old}$ (implicit)

Proof:
(37) $i_{old}\lt s.length\to i_{old}\le s.length-1$ (from (6) and arithmetic)
(38) $j_{old}\ge 0\to -j_{old}\le 0$ (from (1) and arithmetic)
(39) $i\le (s.length-1)-0+1$ (from (37), (38), and (34))
(40) $i\le s.length$ (from (39) and arithmetic)
(41) $i_{old}-j_{old}\ge 0$ (from (1) and arithmetic)
(42) $i\ge 1$ (from (41) and (34))
(43) $0\le j\le t.length$ (from (35), arithmetic, and string length being non-negative)
(44) $i\ge j$ (from (42) and (35))
$I_1$ follows from (42), (40), (43), and (44)

(45) $i - j = (i_{old} - j_{old} + 1) - 0 = i_{old} - j_{old} + 1$ (from (34) and (35))
(46) $0 \le k \le s.length \longrightarrow PartMatch(s[..), t[..), k, 0)$ (Lemma 1)
(47) $0 \le i - j \le s.length \longrightarrow PartMatch(s[..), t[..), i - j, 0)$ (from instantiating (46) with $k = i - j$)
(48) $0 \le i - j \le s.length$ (from $I_1$ proof and (35))
(49) $PartMatch(s[..), t[..), i - j, j)$ (from (47), (48), and substituting $j=0$ from (35))
$I_2$ follows from (49)

(50) $s[(i_{old} - j_{old}) + j_{old}] \neq t[j_{old}]$ (from (33) and arithmetic)
(51) $j_{old} < t.length \land s[(i_{old} - j_{old}) + j_{old}] \neq t[j_{old}] \longrightarrow \neg Matched(s[..), t[..), i_{old} - j_{old})$ (from Lemma 6)
(52) $\neg Matched(s[..), t[..), i_{old} - j_{old})$ (from (51), (5), and (50))
(53) $i_{old} - j_{old} \neq First(s[..), t[..))$ (from (52) and definition of $First$)
(54) $i_{old} - j_{old} < First(s[..), t[..))$ (from (3) and (53))
(55) $i_{old} - j_{old} + 1 \le First(s[..), t[..))$ (from (54) and arithmetic)
(56) $i - j \le First(s[..), t[..))$ (from (45) and (55))
$I_3$ follows from (56)

(57) $\neg found$ (from (7) and (36))
(58) $t.length \gt 0$ (from (5) and (1))
(59) $j \neq t.length$ (from (35) and (58))
(60) $\neg found \leftrightarrow j \neq t.length$ (from (57) and (59))
$I_4$ follows from negating both sides of (60)

Since the invariant $I\triangleq I_1\land I_2\land I_3\land I_4$ is re-established at the end of both case 1 and case 2, and these two cases exhaustively cover the loop body, it has been proven that the loop body successfully maintains the invariant.

## c.
Proof obligation:
$I\land \neg (j\lt t.length\land i\lt s.length\land \neg found)\to M_1\land M_2$
Givens:
(1) $0 \le i \le s.length \land 0 \le j \le t.length \land i \ge j$ (from I)
(2) $PartMatch(s[..), t[..), i-j, j)$ (from I)
(3) $i-j \le First(s[..), t[..))$ (from I)
(4) $found \leftrightarrow j = t.length$ (from I)
(5) $j \ge t.length \lor i \ge s.length \lor found$ (from negation of loop condition)

Proving $M_1$:
(ass1) $found$
(6) $j=t.length$ (from (ass1) and (4))
(7) $PartMatch(s[..),t[..),i-j,t.length)$ (from (6) and (2))
(8) $Matched(s[..),t[..),i-j)$ (from (7) and Lemma 5)
(9) $First(s[..),t[..))\le i-j$ (from (8) and the definition of $First$)
(10) $First(s[..),t[..))=i-j$ (from (9), (3), and arithmetic)
$M_1$ follows from assuming (ass1) and reaching (10)

Proving $M_2$:
(ass2) $\neg found$ 
(11) $j \neq t.length$ (from (ass2) and (4))
(12) $j < t.length$ (from (11) and (1))
(13) $i \ge s.length$ (from (ass2), (12), and (5), since the other two disjuncts are false)
(14) $i = s.length$ (from (13) and (1))
(15) $s.length - j \le First(s[..), t[..))$ (from (14) and (3))
(16) $s.length - j > s.length - t.length$ (from (12) and arithmetic)
(17) $First(s[..), t[..)) > s.length - t.length$ (from (15) and (16))
(18) $First(s[..), t[..)) = s.length \lor First(s[..), t[..)) \le s.length - t.length$ (from Lemma 4)
(19) $First(s[..), t[..)) = s.length$ (from (17) and (18), since the second disjunct is false)
$M_2$ follows from assuming (ass2) and deriving (19)