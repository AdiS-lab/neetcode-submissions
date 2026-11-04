class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
            
        max_reach, cur_reach = 0,0
        jumps = 0

        for i, v in enumerate(nums):
            max_reach = max(max_reach , i + v)

            print(max_reach)
            if max_reach >= (len(nums) - 1):
                jumps += 1
                return jumps

            if i == cur_reach: # reached the end of reach segment
                cur_reach = max_reach
                jumps += 1
        
        return jumps



    
        