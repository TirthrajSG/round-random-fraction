"""

Two numbers X and Y are chosen between 1 and 0.
What is the probability that X/Y will 
round to a even number.

"""

import random
import math

n = 10000000

outcomes_rounded = [0]*n
outcomes_floored = [0]*n
for i in range(n):
    generated_num1 = random.random()
    generated_num2 = random.random()
    rounded_fraction = round(generated_num1/generated_num2)
    floored_fraction = math.floor(generated_num1/generated_num2)
    outcomes_rounded[i] = 1 if rounded_fraction%2==0 else 0
    outcomes_floored[i] = 1 if floored_fraction%2==0 else 0

print("P(faction rounded is even) =", sum(outcomes_rounded)/n)
print("P(faction floored is even) =", sum(outcomes_floored)/n)

# P(faction rounded is even) = 0.4645017
# P(faction floored is even) = 0.6533245
