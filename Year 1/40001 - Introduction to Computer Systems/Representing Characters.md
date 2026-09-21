---
date: 2026-04-05
tags:
  - first-year
  - M40001
---
**Characters** are mapped to specific [[binary]] numbers, as dictated by a chosen **character set**.

**ASCII** **Character Set**:
* Uses $7$ **bits**, granting $128$ possible characters.
	* Modern computers often extend this to $8$ **bits.
* Contains:
	* $26+26$ uppercase and lowercase letters.
	* $10$ digits.
	* $32$ punctuation marks.
	* The remaining $34$ characters represent whitespace, such as space and tab, and control characters.

**Unicode** **Character Set**:
* Aims to represent every character in every language.
* First $127$ characters directly correspond to **ASCII** for backwards compatibility.
* The number of **bits** used varies:
	* UTF-8 is the most common implementation, and uses a variable length of $8$, $16$, $24$, or $32$ **bits** per character.
	* UTF-16 uses a variable length of either $16$ or $32$ **bits**.
	* UTF-32 uses a fixed length of $32$ **bits** for every character.