string = "hello"


def reverseString(string):
    if len(string) == 1:
        return string
    lastElement = string[-1]
    return lastElement + reverseString(string[:-1])


# ----------------------------------------------------
# Efficient Way To Do IT
# ----------------------------------------------------


def efficientReversing(string):
    def actuallReverse(index):
        if index == 0:
            return string[0]
        return string[index] + actuallReverse(index - 1)

    return actuallReverse(len(string) - 1)


print(efficientReversing(string=string))
