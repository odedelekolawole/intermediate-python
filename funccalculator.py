unit_price = float(input("Enter the unit price:  "))
quantity = int(input("Enter the quantity: "))


def calculator(unit_price, quantity):
     total = unit_price * quantity
     return f"Your bill is {total}"
print(calculator(unit_price, quantity))