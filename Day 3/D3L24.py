# Day 3: Lesson 24: 100 Days of Python
# Nested if-else statements and elif statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster.")

    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay ₹40.")
    elif age <= 18:
        print("Please pay ₹70.")
    else:
        print("Please pay ₹120.")

else:
    print("Sorry, you to grow taller before you can ride.")

'''
BMI calculation and its interpretation
'''

weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi >= 25:
    print("overweight")
elif bmi >= 18.25:
    print("normal weight")
else:
    print("underweight")
