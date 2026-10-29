class Solution:
    def findMin(self, nums: List[int]) -> int:

        start = 0 
        end = len(nums)

        init_val = nums[0]

        while start < end:
            mid = (start + end) // 2



            left = nums[mid - 1] if mid else float('-inf')
            right = nums[mid + 1] if mid != len(nums)-1 else float('inf')

            if nums[mid] < left:
                return nums[mid]
                
            elif nums[mid] > right: # two checks whether we've hit minimum
                return right

            elif nums[mid] < init_val: # case that 1 is on left hand side of mid
                end = mid
            else:  # case that 1 is on the right hand side of mid
                start = mid + 1
                init_val = nums[mid]



        return nums[0]
        