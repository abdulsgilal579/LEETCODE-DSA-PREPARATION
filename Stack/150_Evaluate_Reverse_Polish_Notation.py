tokens = ["2", "1", "+", "3", "*"]


def evaluateRPN(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b / a))
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(token))
    return stack[0]


print(evaluateRPN(tokens=tokens))
