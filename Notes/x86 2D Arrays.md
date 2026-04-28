---
date: 2026-04-20
tags:
  - first-year
  - M40005
---
In [[x86 Memory Layout|memory]], **2D arrays** are actually stored in a single **contiguous** row.
* In [[x86]] and [[C]], **row-major ordering** is used, meaning the **rows** are stored one after another in **memory**.
* Essentially the **2D array** becomes a single long [[x86 Arrays|1D array]].
* If we declare `T A[R][C]`, then the total size is just $R\times C\times sizeOf(t)$.

To find a single element, `A[i][j]`, we can use the following formula:
$$Address=A+i\times(C\times K)+(j\times K)$$

For example, let's say we have a $4\times 5$ **array** `pgh` of $4$ **byte** data.
* To return `pgh[row][column]`, the **compiler** ends up doing:
```x86
leaq (%rdi, %rdi, 4), %rax # %rax = 5 * row
addq %rax, %rsi            # %rsi = column + 5*row
movl pgh(, %rsi, 4), %eax  # %eax = Memory[pgh+(column + 5*row) * 4]
```

A different way to build a **2D array**, used in [[Java]] is to construct a single **array**, which holds **pointers** to each **subarray**.
* Since the **main array** stores **pointers**, each **element** is exactly $8$ [[Binary|bytes]].
* The benefit of this approach is that the **rows** can be varying lengths.
A downside of this approach, is we now require two **memory reads** to access the array.
* In general, `T arr[row][col] = Mem[ Mem[arr + 8*row] + sizeOf(T)*col]`

