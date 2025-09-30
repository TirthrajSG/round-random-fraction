# Probability Puzzle: Rounding of a Random Fraction

This repository explores a fascinating probability puzzle through both a numerical simulation and a formal analytical solution.

## The Problem

> Two numbers, X and Y, are chosen uniformly at random from the interval [0, 1]. What is the probability that the fraction Y/X will round to an even number?


## Approaches

1.  **Simulation (`main.py`)**: A Python script that simulates the random process a large number of times to approximate the probability.
2.  **Analytical Solution (`solution.ipynb`)**: A Jupyter Notebook that derives the exact probability using geometric probability and calculus.

---

### 1. Simulation

The `main.py` script uses a Monte Carlo method to estimate the probability. It repeatedly performs the following steps:
1.  Generates a pair of random numbers (X, Y) from a uniform distribution between 0 and 1.
2.  For each pair, it calculates the fraction `Y/X`.
3.  The fraction is rounded to the nearest integer.
4.  It checks if the rounded result is an even number.
5.  The final probability is approximated by the ratio of the number of "even" outcomes to the total number of trials.

### 2. Analytical Solution

The analytical solution involves geometric probability. Choosing two numbers X and Y from [0, 1] is equivalent to picking a random point (X, Y) from a unit square in the Cartesian plane. The probability is the area of the region within this square that satisfies the condition.

The fraction Y/X rounds to a non-negative even integer n (where n = 0, 2, 4, ...) if it falls within the interval:

![](https://quicklatex.com/cache3/19/ql_e463cf4489c2f85d210ba4a19d3b9819_l3.png)

We can find the total favorable area by summing the areas for each case of n.
