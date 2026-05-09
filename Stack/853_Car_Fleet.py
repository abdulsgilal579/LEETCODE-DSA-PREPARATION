target = 100
position = [0, 2, 4]
speed = [4, 2, 1]


def carFleet(t, p, s):
    stack = []
    pairs = sorted(zip(p, s), reverse=True)
    for position, speed in pairs:
        time = (t - position) / speed
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)


print(carFleet(target, position, speed))
