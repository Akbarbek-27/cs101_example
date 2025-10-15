# Problem Statement: The Fibonacci sequence is a famous mathematical sequence where each number is the sum of the two preceding ones. 
# It starts with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... 
# Write a program that asks the user for a quantity (e.g., “how many numbers?”) and then generates and prints that many numbers from the Fibonacci sequence.

# Key Concepts to Apply:
# Getting user input and converting it to an int.
# Using a for loop to iterate a specific number of times.
# Managing and updating multiple variables inside a loop to keep track of the state (the previous two numbers).
# Hint: You’ll need two variables to store the two previous numbers in the sequence, let’s call them a and b. Start them at 0 and 1.
#  Inside your loop, you will:
# Print the current value of a.
# Calculate the next number in the sequence (a + b).
# Update a and b for the next iteration. The old b becomes the new a, and the calculated sum becomes the new b. 
# A clever way to do this in Python is with simultaneous assignment: a, b = b, a + b.
# Example Output:
# --- Fibonacci Sequence Generator ---
# How many Fibonacci numbers would you like to generate? 12
# 0 1 1 2 3 5 8 13 21 34 55 89 

user = int(input("How many numbers?:"))
a = 0
b = 1
for i in range(user):
    print(a, end=" ")
    a, b = b, a + b
