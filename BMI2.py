def calculate_bmi_category():
    weight = float(input("Enter the weight in kilograms: "))
    height = float(input("Enter the height in meters: "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print("BMI:", bmi)
    print("Category:", category)

calculate_bmi_category()
