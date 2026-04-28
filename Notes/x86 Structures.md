---
date:
tags:
  - first-year
  - M40005
---
A `struct` in [[C]] is way of defining **compound data types** made up of other variables, possibly including other **structs**.
* For example:
```C
struct song {
	int lengthInSeconds;
	int yearRecorded
}
```

In [[x86]], a **structure** is stored as a contiguous region in [[x86 Memory Layout|memory]].
* The **compiler** places the **fields** in the exact order that they are declared in the source code, even if this is not the most optimal order.
Because the **order** is fixed, the **compiler** can then determine a permanent offset for each **field**.
* This makes accessing a **field** easy, by simply taking the **base address**, and adding the **fixed offset**.
For example, given this `struct`:
```C
typedef struct rec {
	int a[4];         // 4*4=16 bytes (offset 0)
	long i;           // 8 bytes (offset 16)
	struct rec *next; // 8 bytes (offset 24)
} *rec_p
```
Now, to execute `return r->i`, which is equivalent to `return (*r).i`, where `r` is stored in `%rdi`, the **assembly** is just:
```x86
movq 16(%rdi), %rax
ret
```
Or to compute `r->a[index]`, where `r` is in `%rdi` and `index` is in `%rsi`, we carry out:
```x86
mmovl (%rdi, %rsi, 4), %eax
ret
```

