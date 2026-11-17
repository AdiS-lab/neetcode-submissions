class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
            
        after, before = cost[-1], cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            val1 = cost[i] + after
            val2 = cost[i] + before
            temp = before
            before = min(val1, val2)
            after = temp
        
        return min(after, before)