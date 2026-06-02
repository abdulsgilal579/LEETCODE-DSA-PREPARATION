def recursion(number):
    if number == 1:
        return 1
    return number * recursion(number - 1)


print(recursion(10))
