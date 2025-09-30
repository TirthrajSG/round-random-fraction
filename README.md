# Probability Puzzle: Rounding of a Random Fraction

This repository explores a fascinating probability puzzle through both numerical simulation and formal analytical solution.

## Problems

> **Problem 1:** Two numbers, `X` and `Y`, are chosen uniformly at random from the interval [0, 1]. What is the probability that the fraction `Y/X` will round to an even number?

> **Problem 2:** Two numbers, `X` and `Y`, are chosen uniformly at random from the interval [0, 1]. What is the probability that the floor of the fraction `Y/X` will be an even number?

## Approaches

1. **Simulation (`main.py`)**: A Python script that simulates the random process many times to approximate the probability.
2. **Analytical Solution (`round.ipynb`) and (`floor.ipynb`)**: A Jupyter Notebook that derives the exact probability using geometric probability and calculus.

---

## 1. Simulation

The `main.py` script repeatedly performs the following steps:

1. Generates a pair of random numbers `(X, Y)` from a uniform distribution on [0, 1].
2. Calculates the fraction `Y/X` for each pair.
3. Rounds or floors the fraction to the nearest integer.
4. Checks if the result is an even number.
5. Approximates the final probability as the ratio of "even" outcomes to total trials.


## 2. Analytical Solution

The analytical solution uses geometric probability. Since `X` and `Y` are chosen uniformly from [0, 1], we can visualize this as selecting a random point `(X, Y)` from the unit square [0, 1] × [0, 1]. The probability equals the area of the region within this square where the condition is satisfied.

### Problem 1: Rounding

The fraction `Y/X` rounds to a non-negative even integer `n` (where `n` = 0, 2, 4, ...) when:

<p align="center">
  <img src="https://quicklatex.com/cache3/19/ql_e463cf4489c2f85d210ba4a19d3b9819_l3.png" alt="n - 0.5 < Y/X < n + 0.5"/>
</p>

### Problem 2: Floor Function

The floor of `Y/X` equals a non-negative even integer `n` (where `n` = 0, 2, 4, ...) when:

<p align="center">
  <img src="https://quicklatex.com/cache3/c7/ql_88d5abe55103c4c6393be60f386a7ac7_l3.png" alt="n ≤ Y/X < n + 1"/>
</p>

### Computing the Probability

The total probability is found by:
1. Identifying the regions in the unit square corresponding to each even value of `n`
2. Computing the area of each region
3. Summing these areas to get the total favorable area

The notebook provides detailed calculations with visualizations of these regions.

---
