# Day 1: Lesson 9: 100 Days of Python
# Python Variables

'''
Learn to store values in containers for later use.
Variables is a concept in programming that allows us to give a label to a piece of data so that we can refer or reference that data using the chosen variable name.
We will see in the lesson how to create variables and how to use the variables to access the contained value.
'''

name = input("What is your name? ")
print(name)
print(len(name))

name = "Jack"
print(name)
print(len(name))

# print(len(input("What is your name? ")))
username = input("What is your name? ")
length = len(username)
print(length)

'''
Variable values can be changed.
len() is used to find length of a string.
Debugging tips: explain the code linewise, understand the error written on the terminal
Good practices: Read documentation, read and understand other people's code.
Write readable, reusable and modular pieces of code.
'''

# Exchanging values of two variables.

first = 123
second = 456
(first, second) = (second, first)
