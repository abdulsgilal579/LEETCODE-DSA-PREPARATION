
matrix = [
    [1,  3,  5,  7],    
    [10, 11, 16, 20],   
    [23, 30, 34, 60],   
    [61, 65, 70, 75],   
    [80, 85, 90, 95],   
]

target = 10

def search2dMatrix(matrix, target):
    highPointer = 0
    lowPointer = len(matrix) - 1

    while highPointer <= lowPointer:
        middleArray = (lowPointer + highPointer) // 2
        if matrix[middleArray][0] > target:
            lowPointer = middleArray - 1
        elif matrix[middleArray][-1] < target:
            highPointer = middleArray + 1
        else:
            arrayFound = matrix[middleArray]
            leftPointer = 0
            rightPointer = len(arrayFound) - 1
            while leftPointer <= rightPointer:
                middleElement = (leftPointer + rightPointer)//2
                if arrayFound[middleElement] == target:
                    return True
                elif arrayFound[middleElement] > target:
                    rightPointer = middleElement - 1
                elif arrayFound[middleElement] < target:
                    leftPointer = middleElement + 1
                else:
                    return False
    return False
                

    