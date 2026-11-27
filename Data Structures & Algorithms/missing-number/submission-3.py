class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [1,2,3]
        
        expected_total = 0
        for i in range(1,len(nums)+1):
            expected_total += i

        return expected_total - sum(nums)