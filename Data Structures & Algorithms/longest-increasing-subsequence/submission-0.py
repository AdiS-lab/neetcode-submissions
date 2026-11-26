class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            subproblems = [dp[k] for k in range(i) if nums[k] < nums[i]]
            dp[i] = 1 + max(subproblems, default=0)
        return max(dp, default = 0)






'''
[9,1,4,2,3,3,7]
1 --> 2 --> 3 --> 7

dp = memoization

caching results for recursion
[0,3,1,3,2,3]


'''


