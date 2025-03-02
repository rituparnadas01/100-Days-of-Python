# Day 4: Lesson 31: 100 Days of Python
# Psudorandom number generaotrs

'''
random.randint(a, b): returns a random integer N such that a <= N <= b. Alias for randrange(a, b+1)
random.random(): returns the next random floating-point number in the range 0.0 <= X < 1.0.
random.uniform(a, b): returns a random floating-point number N such that a <= N <= b for a <= b, and b <= N <= a for b < a.
'''

import random

random_integer = random.randint(1, 10)

random_number_0_to_1 = random.random()
random_number_0_to_10 = random.random() * 10

random_float = random.uniform(1,10)

print(random_integer)
print(random_number_0_to_1)
print(random_number_0_to_10)
print(random_float)

'''
Creating and using a Python module
'''
import my_module

print(my_module.my_fav_num)

# Heads or Tails

toss = random.randint(1,2)

if toss == 1:
    print("Heads")
else:
    print("Tails")
    