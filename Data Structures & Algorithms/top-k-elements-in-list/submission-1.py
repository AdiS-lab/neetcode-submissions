class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if nums[i] in check:
                check[nums[i]] += 1
            else:
                check[nums[i]] = 1;
                
        # sort the object and then grab the last k values
        frequencies = sorted(check, key = check.get)
        return frequencies[-k:]
        