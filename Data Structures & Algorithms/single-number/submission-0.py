class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        running_sum = 0 
        for i in range(len(nums)):
            running_sum = running_sum ^ nums[i]
        
        return running_sum