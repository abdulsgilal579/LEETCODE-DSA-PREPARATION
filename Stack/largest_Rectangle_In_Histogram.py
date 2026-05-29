heights = [2, 1, 5, 6, 2, 3]


def largestRectHist(heights):
    stack = []
    maxArea = 0

    for i in range(0, len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            topElement = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            right = i
            width = right - left - 1
            area = width * heights[topElement]
            maxArea = max(maxArea, area)
        stack.append(i)

    while stack:
        right = len(heights)
        topElement = stack.pop()
        if stack:
            left = stack[-1]
        else:
            left = -1
        width = right - left - 1
        area = width * heights[topElement]
        maxArea = max(maxArea, area)
    return maxArea


print(largestRectHist(heights=heights))
