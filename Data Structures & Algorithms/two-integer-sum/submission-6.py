class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            missingVal = target-nums[i]
            if missingVal in check:
                return [check[missingVal], i]
            check[nums[i]] = i;
        return False
        