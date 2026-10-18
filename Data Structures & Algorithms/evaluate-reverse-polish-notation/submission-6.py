import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+": 
                    last = stack.pop()
                    secondLast = stack.pop()
                    stack.append(secondLast + last)
                case "-":
                    last = stack.pop()
                    secondLast = stack.pop()
                    stack.append(secondLast - last)
                case "*":
                    last = stack.pop()
                    secondLast = stack.pop()
                    stack.append(secondLast * last)
                case "/":
                    last = stack.pop()
                    secondLast = stack.pop()
                    stack.append(math.trunc(secondLast / last))
                case _:
                    stack.append(int(t))

        return stack[0]

# don't have to walk through range
# don't have to compute secondLast on every walk
# tokens=["2","1","+","3","*"]
