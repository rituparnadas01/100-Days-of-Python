# Day 3: Lesson 26: 100 Days of Python
# Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 150

if size == "S":
    bill = bill
elif size == "M":
    bill += 50
elif size == "L":
    bill += 100
else:
    print("You typed the wrong inputs.")

if pepperoni == "Y":
    bill += 20
    if size != "S":
        bill += 10

if extra_cheese == "Y":
    bill += 10

print(f"Your final bill is: ₹{bill}.")
