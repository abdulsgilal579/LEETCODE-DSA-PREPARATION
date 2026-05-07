temperatures = [73,74,75,71,69,72,76,73]

def dailyTemperature(temperatures):
    length = len(temperatures)
    stack = [0]
    finalArray = [0]*length

    for temp in range(1, length):
        while stack and temperatures[temp] > temperatures[stack[-1]]:
            popped = stack.pop()
            finalArray[popped] = temp - popped
        stack.append(temp)
    return finalArray

print(dailyTemperature(temperatures=temperatures))


