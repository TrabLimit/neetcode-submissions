class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # keeps the minimum so far at each level
        
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            tmp = min(val, self.minStack[-1])
            self.minStack.append(tmp)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


        
