def sumOfAllDigits(number):
    if number < 10:
        return number
    digit = number % 10
    return digit + sumOfAllDigits(number // 10)


print(sumOfAllDigits(12))
