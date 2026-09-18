class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if(not self.minimum):
            self.minimum.append(val)
        else:
            if(val < self.minimum[-1]):
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[-1])

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minimum = self.minimum[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
