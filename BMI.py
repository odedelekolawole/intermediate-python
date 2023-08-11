# import numpy as np

# < 18.5 under weight
# 18.5 - 24.9 Normal Weight
# 25 - 29.9 Overweigh
# > 30 - You will soon die

# BMI = weight/heightSquare

def bmi(weight, height):
    
    ans = float(weight / (height ** 2))
    print(ans)

    if ans < 18.5:
        print('You are underweigth')
    elif ans < 25:
        print('Normal weight')
    elif ans < 30:
        print('Overweight')
    elif ans > 30:
        print('You will soon die')
    else:
        print("You weigh could not be determined")

weight = float(input("Enter you weight in Kg: "))
height = float(input("Enter the height kg: "))

bmi(weight, height)


# height = int(input("Enter the height cm: "))
# weight = int(input("Enter you weight in Kg: "))
# def BMI(height, weight):
#     bmi_value = weight/((height/100) **2)

#     print(round(bmi_value) 2 )
#     print(bmi_value)

#     if bmi_value < 18.5:
#         print("You are underweight")
#     elif bmi_value in range(18.5, 24.9):
#         print


    
