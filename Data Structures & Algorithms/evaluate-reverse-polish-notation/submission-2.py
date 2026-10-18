class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if len(stack) > 1:
                last = len(stack)-1
                secondLast = len(stack) -2
                match tokens[i]:
                    case "+": 
                        stack[secondLast] = stack[last] + stack[secondLast]
                        stack.pop(last)
                    case "-":
                        stack[secondLast] = stack[secondLast] - stack[last]
                        stack.pop(last)
                    case "*":
                        stack[secondLast] = stack[secondLast] * stack[last]
                        stack.pop(last)
                    case "/":
                        stack[secondLast] = int(stack[secondLast] / stack[last])
                        stack.pop(last)
                    case _:
                        stack.append(int(tokens[i]))
            else:
                stack.append(int(tokens[i]))

        return stack[0]
        