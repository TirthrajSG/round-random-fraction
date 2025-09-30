"""

Two numbers X and Y are chosen between 1 and 0.
What is the probability that X/Y will 
round to a even number.

"""

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