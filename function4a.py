number1 = int(input("Enter the first number: "))
operator = input("Enter the operator: ")
number2 = int(input("Enter the second number: "))


def calculator(number1, operator, number2):
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 / number2
    else:
        print("Invalid operator, enter a correct operator")
        return
    print("Result:", result)
    
calculator(number1, operator, number2)
