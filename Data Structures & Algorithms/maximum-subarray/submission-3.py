class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # only when negative we know that 
        # the max subarray was before

        # if it were ever to go positive again that means
        # that the new subarry afterwards is inherenly greater 
        # than the max of the previous because it ameliorates an offset

        max_sum = nums[0]
        temp_sum = nums[0]

        for v in nums[1:]:
            temp_sum = max(v, v+temp_sum)
            max_sum = max(max_sum, temp_sum)

        return max_sum
            
            


        