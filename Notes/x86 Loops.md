---
date: 2026-04-18
tags:
  - first-year
  - M40005
---
In [[x86]], **loops** must be compiled into a set of [[x86 Conditional Branching|conditional branches]].

Let's first consider a `do-while` loop, such as this one in [[C]]:
```C
int fact_do(int x) {
	int result = 1;
	do {
		result *= x;
		x = x-1;
	} while (x > 1);
	return result;
}
```
We can rewrite this using `goto` like this:
```C
int fact_goto(int x) {
	int result = 1;
Loop:
	result *= x;
	x = x-1;
	if (x>1)
		goto Loop;
	return result;
}
```
And now the **assembly** is obvious:
```x86
fact_do:
	movl $1, %eax    # eax=1
.L2:
	imull %edi, %eax # eax=eax*edi
	subl $1, %edi    # edi-=1
	cmpl $1, %edi    # compare 1 & edi
	jg .L2           # jump if greater
	rep ret          # return
```
* Note `rep ret` is the same as `ret`, and is from a historical quirk.

One way to do a standard **while** loop would be like this:
```C
	goto test;
loop:
	Body
test:
	if (Test)
		goto loop;
done:
```
* This takes our **do-while** code, but starts by jumping to the test.
Here's an example:
* ![[Pasted image 20260418154000.png|553]]

The previous **while** loop requires a **jump** at the start of the loop.
* We can write a new version that only **jumps** in the rare case that the initial test fails.
In **C** it looks like this:
```C
if (!Test)
	goto done;
do
	Body
	while (Test);
done:
```
Or with `goto`:
```C
	if (!Test)
		goto done;
loop:
	Body
	if (Test)
		goto loop;
done:
```
Here's our same **example**, `fact_while`, but with this **optimisation**:
* ![[Pasted image 20260418154240.png|480]]

A **for** loop takes the following form:
```C
for (Init; Test; Update)
	Body
```
Which easily translates to a **while** loop like this:
```C
Init;
while (Test) {
	Body
	Update;
}
```

We've seen both the **goto-middle** and **do-while** ways to translate a **while loop**, and the same applies for a translated **for loop**:
* ![[Pasted image 20260418155649.png|193]]![[Pasted image 20260418155702.png|191]]
As an example of this, can translate this code to calculate **factorial**
```C
for (i=2; i<=n; i++) {
	result *= i
}
```
Into these equivalent loops:
* ![[Pasted image 20260418155901.png|352]]

**C** also provides `break` and `continue`.
* If we use `break`, then the compiler simply **jumps** to the `done:` label.
* To implement `continue`, we want to skip the body, but still run the update step, and so we must add a label at the update step, and **jump** here.