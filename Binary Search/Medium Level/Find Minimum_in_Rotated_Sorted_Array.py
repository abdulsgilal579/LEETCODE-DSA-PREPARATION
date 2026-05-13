rotatedArray = [3,4,5,1,2]


def minimumInRotatedArray(array):
    left = 0
    right = len(array) - 1

    while left <= right:
        middleElement = (left + right) // 2
        if array[middleElement] > array[-1]:
            left = middleElement + 1
        else:
            right = middleElement - 1
    return array[left]

    # What if the 2 elements are like this:
    # [5, 1]
    # Here the right element is the minimum, not the left!
    # So you can't just assume left is always smaller when 2 elements remain. That's exactly why the binary search logic handles it properly — it doesn't assume, it checks nums[mid] > nums[-1] to decide which side to go.

        

