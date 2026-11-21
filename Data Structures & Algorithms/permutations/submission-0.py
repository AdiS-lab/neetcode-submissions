class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 2:
            return [nums]

        res = []

        def dfs(i, permutation):
            if len(permutation) >= len(nums):
                res.append(permutation)
                return 
            
            # idea = call dfs on prepending + appending
            dfs(i + 1, permutation + [nums[i]])
            dfs(i + 1, [nums[i]] + permutation)
            print(permutation)

            for v in range(len(permutation) - 1):
                dfs(i + 1, permutation[0:v+1] +  [nums[i]] +  permutation[v+1:])

            return
        dfs(1, [nums[0]])
        return res

'''


1 -> 1,2 2,1 ->   


'''