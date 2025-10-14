dish1 = "Marine fish" 
dish2 = "Chicken Tikka Masala"
dish3 = "Beef Stroganoff"

price1 = 100.000
price2 = 110.000
price3 = 90.000

quantity1 = int(input(f"Please enter quantity of {dish1}(1,5): " )) 
quantity2 = int(input(f"Please enter quantity of {dish2}(1,5): " )) 
quantity3 = int(input(f"Please enter quantity of {dish3}(1,5):" )) 



customer_name = input("Please enter your name: ")
student_id = input("Please enter student id(yes, no): ")
order_time = int(input("Please enter order time(0,24): "))


subtotal_before_discounts = int(price1 * quantity1 + price2 * quantity2 + price3 * quantity3)

student_discount_eligibility = student_id == "yes"
student_discount_amount = float(student_discount_eligibility * subtotal_before_discounts * 15 / 100)

happy_hour_discount_eligibility =  int(order_time >= 14 and order_time <= 17)
happy_hour_discount_amount = float(subtotal_before_discounts*happy_hour_discount_eligibility * 20 / 100)

main_discount = float(student_discount_amount * (student_discount_amount >= happy_hour_discount_amount) + happy_hour_discount_amount * (happy_hour_discount_amount > student_discount_amount))
subtotal_after_main_discount = subtotal_before_discounts - main_discount

large_order_discount_eligibility = subtotal_after_main_discount >= 150.000 
large_order_discount_amount = float(subtotal_after_main_discount*large_order_discount_eligibility * 5 / 100)


stack = main_discount * (happy_hour_discount_eligibility == student_discount_eligibility) + (happy_hour_discount_amount or student_discount_amount)
total_discounts = float(stack + large_order_discount_amount * (large_order_discount_eligibility == 1))

subtotal = float(subtotal_before_discounts - total_discounts)
service_charge = float(subtotal * 10 / 100)
delivery_fee = 15.000 
final_total = float(subtotal + service_charge + delivery_fee)
total_saved = float(subtotal_before_discounts - subtotal)


print(f"Customer name: {customer_name}, Student id: {student_id}, Order time: {order_time}")
print(dish1)
print(dish2)
print(dish3)
print(f"Subtotal before discounts: {subtotal_before_discounts}")
print(f"Student discount eligibility :{'True,' * (student_discount_eligibility == 1)   + 'False,' * (student_discount_eligibility == 0)}" )
print(f"Student discount ammount:{student_discount_amount}")
print(f"Happy hour discount eligibility and amount:  {'True' * (happy_hour_discount_eligibility == 1) + 'False' * (happy_hour_discount_eligibility == 0)}" )
print(f"Happy hour discount ammount:{happy_hour_discount_amount}")
print(f"Which discount applied(the larger one): {(main_discount),}" )
print(f"Large order discount eligibility: {'True,' * (large_order_discount_eligibility == 1) }")
print(f"Large order dicount ammount: {large_order_discount_amount}")
print(f"Total discounts: {total_discounts}")
print(f"Subtotal after discounts: {subtotal}")
print(f"Service charge amount: {service_charge}")
print(f"Delivery status: {'True,' * (subtotal >= 100.000) + 'False,' * (subtotal<100.000)}" )
print(f"Delivery fee:{ delivery_fee }")
print(f"Final total: {final_total}")
print(f"Total saved: {total_saved}")
