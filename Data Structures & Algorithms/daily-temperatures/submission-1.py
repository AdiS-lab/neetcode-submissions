class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temp)

        for i in range(len(temp)-1):
            stack.append({"n": temp[i], "i": i})
            while len(stack)!=0 and temp[i+1] > stack[len(stack)-1]["n"]:
                
                popIndex = stack[len(stack)-1]["i"]
                res[popIndex] = i+1 - popIndex
                stack.pop()

        return res




# walking through from beg to end
#if curr is greater than change to index - og index
#that means multiple nums will be added to stack
#multiple nums will need to eval against check without looping back through the arr of nums


# order from smallest to largest with indices involved
# if indice is greater and number is greater than subtract
# 