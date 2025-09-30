# Probability Puzzle: Rounding of a Random Fraction

This repository explores a fascinating probability puzzle through both a numerical simulation and a formal analytical solution.

## The Problem

> Two numbers, X and Y, are chosen uniformly at random from the interval [0, 1]. What is the probability that the fraction Y/X will round to an even number?

*Note: Rounding is to the nearest integer. The number 0 is considered an even number.*

## Approaches

Two methods were used to solve this problem:

1.  **Monte Carlo Simulation (`main.py`)**: A Python script that simulates the random process a large number of times to approximate the probability.
2.  **Analytical Solution (`solution.ipynb`)**: A Jupyter Notebook that derives the exact probability using geometric probability and calculus.

---

### 1. Monte Carlo Simulation

The `main.py` script uses a Monte Carlo method to estimate the probability. It repeatedly performs the following steps:
1.  Generates a pair of random numbers (X, Y) from a uniform distribution between 0 and 1.
2.  For each pair, it calculates the fraction `Y/X`.
3.  The fraction is rounded to the nearest integer.
4.  It checks if the rounded result is an even number.
5.  The final probability is approximated by the ratio of the number of "even" outcomes to the total number of trials.

#### Code Snippet (`main.py`)
```python
import random

testcases = 5
n = 100000

for t in range(testcases):

    outcomes = [0]*n
    for i in range(n):
        generated_num1 = random.uniform(0,1)
        generated_num2 = random.uniform(0,1)
        rounded_fraction = round(generated_num1/generated_num2)
        outcomes[i] = 1 if rounded_fraction%2==0 else 0

    print(sum(outcomes)/len(outcomes))