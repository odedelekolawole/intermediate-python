print("Create Account Now")
username  = input('Enter your username:   ')
password  = input('Enter your password:   ')

if  len(password) > 8 and '*, -, %, .,' in password:
    print('login succesfully')
else:
    print('Password to short or does not contain special character')

