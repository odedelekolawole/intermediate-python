# name of student 
# age
# gender
# class jss1 to ss3






# students = ["Kolawole", 20, 'JSS1', 'JSS2', 'JSS3', 'F', "M", "Frontend", "Backend"]

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# your_class = input("Enter your class: ")


# # def registration(name, age, gender, your_class):
# #     student_list = []
# #     for item in students:
# #         if item not in students:
# #             student_list.append(name, age, gender, your_class)
# #         elif item in students:
# #             return f"You are already in the student registration portal"
# #     return student_list.append(name, age, gender, your_class)
# # print(registration(name, age, gender, your_class))



# students = ["Kolawole", 20, 'JSS1', 'JSS2', 'JSS3', 'F', "M", "Frontend", "Backend"]

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender: ")
# your_class = input("Enter your class: ")


# def registration(name, age, gender, your_class):
#     student_list = []
#     for item in students:
#         if name not in students:
#             student_list.append(name, age, gender, your_class)
#         elif item in students:
#             return f"You are already in the student registration portal"
#     return student_list.append(name, age, gender, your_class)
# print(registration(name, age, gender, your_class))

students = []
def student_registration():
    count = 0
    while count < 2:
        name = input("Enter your name:  ")
        if name not in students:
            students.append(name)
            age = int(input("Enter your age:  "))
            gender = int(input("\n 1. Male  \n 2. Female \n"))
            course = int(input("\n 1. Backend  \n 2. Frontend \n 3. Ethical Hacking \n 4. Product Design \n 5. Data Science \n"))
        else:
            print("You are alread a registered student")
        print(students)
        count + 1
print(student_registration())