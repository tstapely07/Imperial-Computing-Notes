---
date: 2026-04-09
tags:
  - first-year
  - M40001
---
Sometimes we need to add [[binary]] numbers that are being transmitted as **serial data**.
* Instead of using a [[Serial and Parallel Conversion|serial to parallel converter]], followed by a normal [[ripple through carry adder]], and then a **parallel to serial converter**, we can use a **serial adder**.
* This assumes the **bits** arrive starting with the **least significant bits**.
The [[Sequential Circuits|circuit]] uses a single [[Edge-Triggered D-Type Flip-Flop|edge-triggered D-type flip-flop]]:
* ![[Pasted image 20260409165736.png|391]]