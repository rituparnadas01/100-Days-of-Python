# Day 2: Lesson 15: 100 Days of Python
# Type Error, Type Checking a Type Conversion

'''
TypeError: You can't put a rock inside a potato processor, it will give type error.
A function should always be provided with the right kind of data type to give out results.
Use type() to check data type of the primitive data.
'''

print(len("123")) # Without quotes, this gives TypeError.
print(type(123))


'''
Write out 4 type checks to print all 4 data types.
'''

holiday = "Venice"
age = 55
bill_in_dollars = 125_000.599
did_you = False

print(type(holiday))
print(type(age))
print(type(bill_in_dollars))
print(type(did_you))


'''
Converting one data type into another.
'''

print(type("123"), type(int("123")))
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# ValueError  (for example, when you try to convert alphabets into integer data types)
