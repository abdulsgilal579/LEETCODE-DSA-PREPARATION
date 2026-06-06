array = [8, 3, 12, 5, 9999.4, 9999.5]


def maximumRecursion(array):
    def maximum(index):
        if index == 0:
            return array[0]
        return max(array[index], maximum(index - 1))

    return maximum(len(array) - 1)


print(maximumRecursion(array=array))


# Stack Call
# maximum(5)
# = max(7, maximum(4))
#
# maximum(4)
# = max(20, maximum(3))
#
# maximum(3)
# = max(5, maximum(2))
#
# maximum(2)
# = max(12, maximum(1))
#
# maximum(1)
# = max(3, maximum(0))
#
# maximum(0)
# = 8
#
# Unwinding:
#
# max(3, 8)   = 8
# max(12, 8)  = 12
# max(5, 12)  = 12
# max(20, 12) = 20
# max(7, 20)  = 20
