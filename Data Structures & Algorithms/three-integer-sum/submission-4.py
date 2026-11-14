class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1 

            while l < r:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    r -= 1
                    l += 1
                
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif three_sum > 0:
                    r -= 1
                else:
                    l+= 1
        return res
