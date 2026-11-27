class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # [1,2,3]
        
        actual_total, expected_total = 0, 0
        for i in range(1,len(nums)+1):
            expected_total += i

        for n in nums:
            actual_total += n
        
        print(f"{actual_total=} and {expected_total=}")
        difference = expected_total - actual_total 
        return 0 if difference < 0 else difference