class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()

        backtrack([])
        return res
                


'''

[1,2,3]

path = [1] --> [1,2] --> [1,2,3]
           --> [1,3] --> [1,3,2]
        [2] --> [2,1] --> [2,1,3]

'''
        