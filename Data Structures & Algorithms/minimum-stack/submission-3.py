import math
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val
        return None
        
    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) == 0:
            self.min = math.inf
        else:
            self.min = sorted(self.stack)[0]

        return None
        
    def top(self) -> int:
        if len(self.stack) == 0:
            return 0      
        return self.stack[len(self.stack)-1]  

    def getMin(self) -> int:
        return self.min
# edge case where min is inf, where you have 0 and then
# try to get a min

        
