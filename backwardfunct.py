def backward(my_list):
    list_reverse = []
    for value in range(len(original_list)):
        list_reverse.append(original_list.pop())
    return "List after reversal :", list_reverse
original_list = ["a", "b", "c", "d"]
print(backward(original_list))