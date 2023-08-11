
# total_attempts = 0
username = input("Enter a username: ")
no_trials = 3
max_no_trials = 3

while len(username) < 8 and no_trials < max_no_trials:
    username = input("Enter a username: ")
    print("username is too short")
    no_trials += 1


