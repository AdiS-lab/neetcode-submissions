class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices) + 2)

        for i in range(len(prices)-1,-1,-1):
            max_total = dp[i+1]
            for j in range(i +1,len(prices)):
                max_total = max(max_total, prices[j] + dp[j+2] - prices[i])
            
            dp[i] = max_total
        
        return dp[0]
