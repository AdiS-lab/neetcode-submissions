class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # sort, smash
        # sort smash

        i = len(stones) - 1
        stones.sort() 

        # [1]

        while len(stones) > 1:
            print(i)
            if stones[i] > stones[i-1]:
                g = stones.pop()
                l = stones.pop()
                stones.append(g - l)
                i -= 1
            else:
                stones.pop()
                stones.pop()
                i -= 2
            
            stones.sort()
        
        return stones[0] if len(stones) > 0 else 0