for n in range(0, 41, 2):
    empty = []
    empty1 = []
    if n % 2 == 0:
        print(n)
        if n % 3 == 0:
            empty.append(n)
            print(empty, f"is divisible by 3")
            if n % 4 == 0:
                empty1.append(n)
                print(empty, f"is divisible by 4")


