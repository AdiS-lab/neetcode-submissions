class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        after, before = nums[-1], nums[-2]

        for i in range(len(nums) - 3, -1, -1):
            possible = nums[i] + after
            temp = before
            before = possible
            after = max(after, temp)

        return max(after, before)