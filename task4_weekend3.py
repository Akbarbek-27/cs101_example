# Problem Statement: This is a classic programming interview question. Write a program that prints the numbers from 1 to 100, each on a new line. 
# However, for multiples of three, print “Fizz” instead of the number. For multiples of five, print “Buzz”. 
# For numbers which are multiples of both three and five, print “FizzBuzz”.

# Key Concepts to Apply:
# A for loop using range(1, 101).
# The modulo operator (%) to check for divisibility.
# A carefully ordered if-elif-else statement. The order matters!
# Hint: The most important part of this problem is the order of your checks. 
# If you check for divisibility by 3 before you check for divisibility by both 3 and 5, you will never print “FizzBuzz”.
#  The most specific condition (number % 3 == 0 and number % 5 == 0) must be checked first.

# Example Output (showing the first 16 lines):
# --- FizzBuzz Challenge (1-100) ---
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# ...
for i in range(1,101):
    if not i % 15:
      print("FizzBuzz")
    elif not i % 3:
        print("Fizz")
    elif not i % 5:
        print("Buzz")
    else:
        print(i)
