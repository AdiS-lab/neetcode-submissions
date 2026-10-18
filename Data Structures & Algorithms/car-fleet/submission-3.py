import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        check = []
        for i in range(len(position)):
            check.append({'p': position[i], 's': speed[i]})
        
        sortedArr = sorted(check, key=lambda c: c['p'])
        # 1:3, 4:2
        for j in range(len(sortedArr)-1,0,-1):
            s1 = sortedArr[j]['s'] # 2
            p1 = sortedArr[j]['p'] 

            s2 = sortedArr[j-1]['s'] # 3
            p2 = sortedArr[j-1]['p']

            if s2 > s1:
                sect = ((p1-p2)/(s2-s1))
                if s1*sect + p1 <= target:
                    sortedArr.pop(j-1)

        return len(sortedArr)
                




# [0, 1, 4, 7] [1, 2, 2, 1]
# 2 > 1 
# 7 - 4 / (2 - 1) = 3
# pop 4 to just get 7

# 

