array = [3, 7, 2, 9, 1]


def sumOfArrayElements(array):
    def summation(index):
        if index == 0:
            return array[index]
        return array[index] + summation(index - 1)

    return summation(len(array) - 1)


print(sumOfArrayElements(array=array))

# Stack
# summation(4)
# = 1 + summation(3)
#
# = 1 + 9 + summation(2)
#
# = 1 + 9 + 2 + summation(1)
#
# = 1 + 9 + 2 + 7 + summation(0)
#
# = 1 + 9 + 2 + 7 + 3
#
# = 22
