number = float(input("Please enter your number:"))
accumulator = 0
while number != 'done':
    accumulator += float(number)
    print(accumulator)
    number = input("Please enter your number or'done':")
    if number == 'done':
        print(f"The final sum of all numbers is:{accumulator}")
        break
