# def greeting(first_name, last_name):
#     print(f"Hello {first_name}, {last_name}")
# greeting('Princewill', 'Daniels')








# def profile(firstname, email):
#     print(f"Welcome to 6B4 {firstname} ")
# profile('Kolawole', 'odedele.kolawole@gmail.com')


# def square(num):
#     result = num * num
#     print(result)
# square(2)



# def finder(list):
#     print(min(list), max(list), len(list), sum(list))
# list_given = [1 , 2, 3]
# finder(list_given)


def multiplier(list):
    total = []
    for n in list:
        n = n ** 2
        total.append(n)
    print(total)
list_given = [1, 2, 3] 
multiplier(list_given)


def varifier(num):
    if num % 2 == 0:
        print(f'{num} is even number')
    else:
        print(f'{num} is odd')
varifier(2)

def check(numbers):
    for n in numbers:
        if n in list_given % 2 == 0:
            print(n)
        else:
            print(numbers)
list_given = [1, 2, 3]
check(list_given)