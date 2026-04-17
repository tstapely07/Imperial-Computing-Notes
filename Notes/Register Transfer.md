---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
One important operation in a **CPU** is transferring data between [[registers]], denoted $R_{destination}\leftarrow R_{source}$.

Selecting the **source register** is done using [[Multiplexers|multiplexers]], with one for each [[Binary|bit]] of the **register**.
* If we have, say, $8$ registers, we will need $8$-to-$1$ **multiplexers.**
* We could construct one using [[functional design]] by combining two $4$-to-$1$ **multiplexers**, each with an **enable** input:
	* ![[Pasted image 20260409154806.png|372]]
* Then each **bit** $i$ is connected as follows:
	* ![[Pasted image 20260409154839.png|288]]

To select the **destination register**, we can make use of the fact that an [[Edge-Triggered D-Type Flip-Flop|edge-triggered D-type flip-flop]] will only write a **bit** on the falling edge of a [[Clocks|clock pulse]].
* Using this, we use a [[Decoders|decoder]] to only apply a **clock pulse** to the destination register.
Again, we can combine two $2$-to-$4$ **decoders** to make a $3$-to-$8$ **decoder**:
* ![[Pasted image 20260409155425.png|346]]

Combining the **source selection** and **destination selection** we get our final **register transfer** circuit:
* ![[Pasted image 20260409155445.png|360]]