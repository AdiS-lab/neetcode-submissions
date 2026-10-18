import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda last, secondLast: secondLast + last,
            "-": lambda last, secondLast: secondLast - last,
            "*": lambda last, secondLast: secondLast * last,
            "/": lambda last, secondLast: math.trunc(secondLast / last)
        }
        for t in tokens:
            if t in operations:
                last = stack.pop()
                secondLast = stack.pop()
                stack.append(operations[t](last, secondLast))
            else:
                stack.append(int(t))

        return stack[0]

# don't have to walk through range
# don't have to compute secondLast on every walk ( can just pop )
# 