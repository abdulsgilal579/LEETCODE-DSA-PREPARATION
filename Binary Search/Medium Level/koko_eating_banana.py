from math import ceil

piles = [3, 6, 7, 11]
hours = 8


def kokoEatingBanan(piles, hours):
    maxPile = max(piles)
    k = [x for x in range(1, maxPile + 1)]
    leftPointer = 0
    rightPointer = len(k) - 1
    minimum = maxPile

    while leftPointer <= rightPointer:
        middleElement = (leftPointer + rightPointer) // 2
        totalHours = 0
        for x in piles:
            totalHours += ceil(x / k[middleElement])
        if totalHours > hours:
            leftPointer = middleElement + 1
        else:
            minimum = min(minimum, k[middleElement])
            rightPointer = middleElement - 1
    return minimum


print(kokoEatingBanan(piles=piles, hours=hours))
