class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        endPointer = len(nums)-1
        startPointer = 0
        while startPointer != endPointer:
            res = nums[startPointer] + nums[endPointer]
            if res == target:
                return [ startPointer+1, endPointer+1 ]
            elif res > target:
                endPointer -= 1;
            
            else:
                startPointer += 1
        return False


        