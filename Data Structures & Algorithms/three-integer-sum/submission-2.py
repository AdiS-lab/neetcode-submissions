class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # [-1,-1,0,1,2,4]

        # if sum >= 0 then move on 
        # if there is a repeat index skip it
        nums.sort()
        res = []

        for i in range(len(nums) - 2): # final indice - 3 stops there
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]: # skip repeated values [-1,-1]
                continue
            
            l = i+1
            r = len(nums) - 1 
        
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
            
                if three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
                