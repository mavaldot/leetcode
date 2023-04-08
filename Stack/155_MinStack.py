class MinStack:

    def __init__(self):
        self.stk = []
        self.curMin = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        minVal = inf
        if self.curMin: minVal = self.curMin[-1]
        self.curMin.append(min(minVal, val))

    def pop(self) -> None:
        self.stk.pop(-1)
        self.curMin.pop(-1)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.curMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()