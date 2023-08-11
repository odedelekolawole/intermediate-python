# def daily_payment(hours_work):
#     payment = hours_work * 2000
#     return f"Your pay is £{payment}"
# hours_work = int(input("How maany hour did you work?    "))
# print(daily_payment(hours_work))


# def daily_payment(hours_work, rate):
#     payment = hours_work * rate
#     return f"Your pay is £{payment}"
# hours_work = int(input("How maany hour did you work?    "))
# rate = int(input("How much is your rate?    "))
# print(daily_payment(hours_work, rate))

# def payment(labours):
#     for labour in labours:
#         if labour == "Bricklayer":
#             return 

# labours = {
#     "Bricklayer": 1000,
#     "Tiler": 1500,
#     "Painter": 2000,
#     "Plumber": 2500
# }




# def payment(category, hour):
#     for element in categories:
#         if category in categories ==  True:
#             payment1 = hour * 1000
#             return payment1
#         elif category in categories True:
#             payment2 = hour * 1500
#             return payment2
#         elif category in categories  True:
#             payment3 = hour * 2000
#             return payment3
#         elif category in categories  True:
#             payment4 = hour * 2500
#             return payment4


# categories = ['bricklayer', 'tiller', 'painter', 'plumber' ]

# category = input("Enter your categoty: ")
# hour = input("Enter yout hour: ")
# print(payment(category, hour))

print('Choose your category number:  "Bricklayer = 1", "Tiller = 2", "Painter = 3", "Plumber = 4"')
categories = {'Bricklayer': 1000, 'Tiller': 1500, 'Painter': 2000, 'Plumber': 2500}
def payment(category, hour):
        # if category not in range(5):
        #      print("You are a ghost worker get out of the paying queue")
        if category == 1:
            return f"Your pay is £{categories['Bricklayer'] * hour}"
        elif category == 2:
            return f"Your pay is £{categories['Tiller'] * hour}"
        elif category == 3:
            return f"Your pay is £{categories['Painter'] * hour}"
        elif category == 4:
            return f"Your pay is £{categories['Plumber'] * hour}"
        else:
             print("Worker not recognised") 
category = int(input("Enter your category or your category number: "))
hour = int(input("Enter your work hour: "))
print(payment(category, hour))

# print("1. Bricklayer \n 2. Tiller \n 3. Painter \n")