number1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
number2 = int(input("Enter the second number: "))

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def calculator(number1, operator, number2):
    if operator == "+":
        result = add(number1, number2)
    elif operator == "-":
        result = sub(number1, number2)
    elif operator == "*":
        result = mul(number1, number2)
    elif operator == "/":
        result = div(number1, number2)
    else:
        print("Invalid operator, enter a correct operator")
        return
    print("Result:", result)

calculator(number1, operator, number2)
