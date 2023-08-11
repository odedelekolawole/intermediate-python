# username = input("Enter the first trial:  ")
# number_of_trials = 0
# max_number_of_trials = 3

# while number_of_trials < max_number_of_trials:
#     print("Username is too short")
#     username = input("Enter a username: ")
#     number_of_trials += 1


username = input("Enter your username")
new_list = [0]
while len(username) < 8 and sum(new_list) !=2:
    username = input("Enter sa username")
    new_list.append(1)