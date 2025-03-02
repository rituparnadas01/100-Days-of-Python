# Day 3: Lesson 25: 100 Days of Python
# We can use multiple if statements in succession and/or use a Boolean flag.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cms? "))

if height >= 120:
    print("You can ride the rollercoaster.")
    default_bill = 40

    age = int(input("What is your age? "))

    if age <= 12:
        bill = default_bill
        print(f"Child tickets are ₹{bill}.")  
    elif age <= 18:
        bill = default_bill + 30
        print(f"Youth tickets are ₹{bill}.") 
    else:
        bill = default_bill + 80
        print(f"Adult tickets are ₹{bill}.") 
    
    flag = False
    photo = (input("Do you want a photo taken? ")).lower()
    if photo == "yes" or "y":
        flag = True
    
    if flag:
        bill += 10

    print(f"Your final bill is ₹{bill}.")

else:
    print("Sorry you have to grow taller before you can ride.")
