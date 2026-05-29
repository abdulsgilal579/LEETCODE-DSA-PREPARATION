nums1 = [1, 4, 7, 10]
nums2 = [2, 3, 5, 6, 8]


def findingFit(a1, a2):
    left = 0
    right = len(a1) - 1

    while left <= right:
        middleElement = (left + right) // 2
        if a1[middleElement] > a2[0]:
            right = middleElement
