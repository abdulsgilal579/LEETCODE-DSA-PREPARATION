class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> int:
        if not self.stack2:
            while self.stack:
                item = self.stack.pop()
                self.stack2.append(item)
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack:
                item = self.stack.pop()
                self.stack2.append(item)
        return self.stack2[-1]

    def empty(self) -> bool:
        if not self.stack and not self.stack2:
            return True
        return False
        