array = [3,1]
target = 1

def searchInRotatedArray(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middleElement = (left + right) // 2
        if array[middleElement] == target:
            return middleElement
        if array[left] <= array[middleElement]: #This means the left array is sorted
            if array[left] <= target <= array[middleElement]: #This means target lies in the left
                right = middleElement - 1
            else: #This means the target can't be in the left
                left = middleElement + 1
        else:
            if array[middleElement] <= target <= array[right]:
                left = middleElement + 1
            else:
                right = middleElement - 1
    return -1

print(searchInRotatedArray(array=array, target=target))