
# def filtering(another):
#     new_list = []
#     return new_list.append(filter(numbers))

# filtering(numbers)



# numbers = [1, 2, 5, 6, 7, 8, 8, 8, 9]
# empty = []

# def filtering(numbers):
#     for number in numbers:
#         if number not in empty:
#             empty.append(number)
#     return empty
# print(filtering(numbers))

def even(numbers):
    even = []
    for digit in numbers:
        if digit % 2 == 0:
            even.append(digit)  
    return even
numbers = [1, 2, 5, 6, 7, 8, 8, 8, 9, 10, 11, 22, 23, 72]
print(even(numbers))
