class Solution:
    def isValid(self, s: str) -> bool:
        endCheck = {')': '(', ']':'[','}':'{'}
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] in endCheck and len(stack) > 0 and stack[len(stack)-1] == endCheck[s[i]]:
                stack.pop()
            else:
                return False   

        if len(stack)>0:
            return False
        return True

# s = "()[]{}"
# s = "([{}])"
# s = "("
# store and when hitting the other pop from stack. 
# if another pops BEFORE HAND then BAD
# "([)]" ==> (, then [, then )

                