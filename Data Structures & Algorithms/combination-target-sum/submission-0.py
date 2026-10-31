class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i, total):
            if total == target:
                res.append(cur.copy())
                return
            if i > len(nums) -1  or total > target:
                return
            
            # repeating decision
            cur.append(nums[i])
            dfs(i, total + nums[i])

            # non repeating decision
            cur.pop()
            dfs(i + 1, total)


        dfs(0, 0)
        return res