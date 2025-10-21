#  Create a shopping cart system that calculates prices with various discounts. Your program should:

# Define a function calculate_item_total(quantity, unit_price) that returns the total price for an item
# Define a function apply_bulk_discount(total, quantity) that:
# Returns 10% discount if quantity >= 10
# Returns 5% discount if quantity >= 5
# Returns 0 otherwise
# Define a function calculate_tax(subtotal, tax_rate) that calculates tax amount
# Define a function calculate_tax(subtotal, tax_rate) that returns True if subtotal >= 50
# Define a function process_order(item_name, quantity, unit_price, tax_rate) that:
# Calculates item total
# Applies bulk discount
# Calculates tax
# Checks shipping eligibility
# Prints a formatted receipt
# Test with these orders:
# “Notebooks”: 12 units at $3.50 each, 8% tax
# “Pens”: 6 units at $1.25 each, 8% tax
# “Paper”: 3 reams at $4.99 each, 8% tax
print("SHOPPING CART CALCULATOR")
print("========================================\n")
def  calculate_item_total(quantity, unit_price):
    return quantity * unit_price
def apply_bulk_discount(total, quantity):
    if quantity > 9:
        return (total * 1/10) 
    elif quantity > 4:
        return (total * 1/20)
    else:
        return 0
def calculate_tax(subtotal, tax_rate):
    return subtotal * tax_rate / 100
def  is_eligible_for_free_shipping(subtotal):
    if subtotal < 50:
        return (f"Need ${50 - subtotal} more for free shipping")
    return subtotal >= 50
def process_order(item_name, quantity, unit_price, tax_rate):    
    print(f"Order Receipt for:{item_name}")
    print(f"Quantity:{quantity}")
    item_total = calculate_item_total(quantity, unit_price)
    print(f"Item total:{item_total}")
    print(f"Bulk discount:{apply_bulk_discount (item_total, quantity)}")
    subtotal = item_total - apply_bulk_discount (item_total, quantity)
    print(f"Subtotal:{subtotal:.2f}")
    print(f"Tax(8%):{calculate_tax(subtotal, tax_rate):.2f}")
    final_total = subtotal + calculate_tax(subtotal, tax_rate) 
    print(f"Final total:{final_total:.2f}")
    print(f"Checking shipping eligibility:{is_eligible_for_free_shipping(subtotal)}")
process_order('Notebooks',12,3.50,8)
process_order('Notebooks',6,1.25,8)
process_order('Notebooks',3,4.99,8)
