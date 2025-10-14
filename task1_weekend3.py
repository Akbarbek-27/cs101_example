price_young = 8
price_adult = 15
price_senior = 10
user = int(input("Please write your age:"))
if user < 13:
    print("You fall into the 'Children' category")
    print(f"Your ticket value:{price_young}$")
elif user < 65:
    print("You fall into the 'Adult' category")
    print(f"Your ticket value:{price_adult}$")
else:
    print("You fall into the 'Senior' category")
    print(f"Your ticket value:{price_senior}$")
print("---Movie Ticket Pricer---")
