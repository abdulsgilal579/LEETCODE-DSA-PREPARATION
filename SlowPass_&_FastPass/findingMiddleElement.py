#I Learned This Today

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def middleElement(array):
    slow = 0
    fast = 0

    while fast + 1 < len(array):
        slow += 1
        fast += 2

    return array[slow]

print(middleElement(array=array))  