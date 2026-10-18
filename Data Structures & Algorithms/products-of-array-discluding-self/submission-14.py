class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # print(f"this is prefix {prefix}")

        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
    
        return res 
 

# check = [1]
#        for i in range(1, len(nums)):
#            temp = check[i-1] * nums[i-1]  
#            check = [x * nums[i] for x in check]
#            check.append(temp) 
#        return check 

