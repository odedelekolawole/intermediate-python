def check(items):
    empty = []
    empty1 = []
    empty2 = []
    empty3 =[]
    for digit in items:
        if digit % 2 == 0:
            empty.append(digit)
    print(empty)
    for digit in items:
        if digit % 3 == 0:
            empty1.append(digit)
    print(empty1)
    for digit in items:
        if digit % 4 == 0:
            empty2.append(digit)
    print(empty2)
    for digit in items:
        if digit % 6 == 0:
            empty3.append(digit)
    print(empty3)
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
check(given_list)
