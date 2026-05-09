nums = [-1,0,3,5,9,12]
target = 9

def binarySearch(nums, target):
    left = 0
    right = len(nums) -1
    while left <= right:
        middleElement = (right + left)//2
        if nums[middleElement] == target:
            return middleElement
        elif nums[middleElement] > target:
            right = middleElement -1
        else:
            left = middleElement + 1
    return -1

print(binarySearch(nums=nums, target=target))
            
    



