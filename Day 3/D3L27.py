# Day 3: Lesson 27: 100 Days of Python
# Logical Operators: and, or, not

a = 12
print(a > 15)
print(a > 10)
print(a > 10 and a > 15)
print(a > 10 or a > 15)
print(not a > 15)

# Give free tickets to people with Midlife crisis:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    bill = 0

    age = int(input("What is your age? "))

    if age <= 12:
        bill += 40
        print(f"Child tickets are ₹{bill}.")  
    elif age <= 18:
        bill += 70
        print(f"Youth tickets are ₹{bill}.") 
    elif 45 <= age <= 55:
        print("Everything is goign to be ok. Have a free ride on us!")
    else:
        bill += 120
        print(f"Adult tickets are ₹{bill}.") 
    
    photo = input("Do you want a photo taken? Y or N: ")
    if photo == "Y":
        bill += 10

    print(f"Your final bill is ₹{bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")
