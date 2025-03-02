# Day 4: Lesson 33: 100 Days of Python
# Who will pay the bill?

import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
N = len(friends)

index_of_bill_payer = random.randint(0, N-1)
name = friends[index_of_bill_payer]

print(f'{name} will pay the bill.')

# Alternatively, using random.choice(L)

print(f'{random.choice(friends)} will pay the bill.')
