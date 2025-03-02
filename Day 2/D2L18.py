# Day 2: Lesson 18: 100 Days of Python
# Tip Calculator

print("Welcome to the tip calculator!")

total_bill = float(input("What is the total bill? ₹"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

tip_percent = tip / 100

num_of_people = int(input("How many people to split the bill? "))

split_bill = (total_bill + tip_percent * total_bill) / num_of_people

print(f"Each person should pay: ₹{round(split_bill, 2)}")
