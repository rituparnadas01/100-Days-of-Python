# Day 2: Lesson 17: 100 Days of Python
# Number manipulation and F strings in Python

'''
Flooring a number
Rounding a number
Assignment operators
F-strings
'''

weight = 50
height = 0.6
height += 1   # assignment operator

bmi = weight / height ** 2

print(bmi)
print(int(bmi))
print((round(bmi)))
print((round(bmi, 2)))  # Rounding upto 2 decimal places
print(f"The BMI is {round(bmi)}.")   # F-strings

print(type(10%3))
print(type(10%3.1))
