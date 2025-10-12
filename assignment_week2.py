dish1 = "Marine fish" 
dish2 = "Chicken Tikka Masala"
dish3 = "Beef Stroganoff"

price1 = 100.000
price2 = 110.000
price3 = 90.000
quantity = int(input("Please enter quantity of dish(1,5): "))


customer_name = input("Please enter your name: ")
student_id = input("Please enter student id(yes, no): ")
order_time = int(input("Please enter order time(0,24): "))
choose = input(f"Please choose dish: {dish1},{dish2},{dish3}:")

buy1 = price1 if choose == dish1 else 0
buy2 = price2 if choose == dish2 else 0
buy3 = price3 if choose == dish3 else 0

subtotal_before_discounts = int(buy1 * quantity + buy2 * quantity + buy3 * quantity)

student_discount_eligibility = student_id == "yes"
student_discount_amount = float(student_discount_eligibility * subtotal_before_discounts * 15 / 100)
happy_hour_discount_eligibility =  int(order_time >= 14 and order_time <= 17)
happy_hour_discount_amount = float(subtotal_before_discounts*happy_hour_discount_eligibility * 20 / 100)
large_order_discount_eligibility = subtotal_before_discounts >= 150.000 
large_order_discount_amount = float(subtotal_before_discounts*large_order_discount_eligibility * 5 / 100)


main_discount = float(student_discount_amount * (student_discount_amount >= happy_hour_discount_amount) + happy_hour_discount_amount * (happy_hour_discount_amount > student_discount_amount))
stack = main_discount if happy_hour_discount_eligibility == student_discount_eligibility else happy_hour_discount_amount or student_discount_amount
total_discounts = float(stack + large_order_discount_amount if large_order_discount_eligibility == 1 else stack)

subtotal = float(subtotal_before_discounts - total_discounts)
service_charge = float(subtotal * 10 / 100)
delivery_fee = 15.000 * (subtotal >= 100.000)
final_total = float(subtotal + service_charge + delivery_fee)
total_saved = float(subtotal_before_discounts - subtotal)



print(f"Customer name: {customer_name}, Student id: {student_id}, Order time: {order_time}")
print(dish1)
print(dish2)
print(dish3)
print(f"Subtotal before discounts: {subtotal_before_discounts}")
print(f"Student discount eligibility and amount: True, {student_discount_amount}" if student_discount_eligibility == 1 else 'Student discount eligibility:False')
print(f"Happy hour discount eligibility and amount: True, {happy_hour_discount_amount}" if happy_hour_discount_eligibility == 1 else 'Happy hour discount eligibility and amount:False')
print(f"Which discount applied(the larger one): {main_discount}" if happy_hour_discount_eligibility == student_discount_eligibility else '' )
print(f"Large order discount: True, {large_order_discount_amount}" if large_order_discount_eligibility == 1 else'' )
print(f"Total discounts: {total_discounts}")
print(f"Subtotal after discounts: {subtotal}")
print(f"Service charge amount: {service_charge}")
print(f"Delivery fee with free delivery status: True, {delivery_fee }" if subtotal >= 100.000 else "Delivery fee with free delivery status:False")
print(f"Final total: {final_total}")
print(f"Total saved: {total_saved}")
