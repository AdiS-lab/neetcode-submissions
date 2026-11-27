class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2 ** 31
        MAX = 2 ** 31
        X = abs(x)

        res = []
        while X > 0:
            res.append(X%10)
            X = X//10
        
        num = 0
        for i, n in enumerate(res):
            num += n*(10**(len(res) -1 - i))
        
        if x < 0:
            num *= -1

        return num if num > MIN and num < MAX else 0
            
        