nums1 = [2, 4, 6]
nums2 = [1, 3, 2, 5, 4, 6]


def nGE(nums1, nums2):
    stack = []
    hashMap = {}
    answer = []

    for nums in nums2:
        while stack and nums > stack[-1]:
            topElement = stack.pop()
            hashMap[topElement] = nums
        stack.append(nums)

    for elements in stack:
        hashMap[elements] = -1

    for nums in nums1:
        if nums in hashMap:
            answer.append(hashMap[nums])
    return answer


print(nGE(nums1=nums1, nums2=nums2))
