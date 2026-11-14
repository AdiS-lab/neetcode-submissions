class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0 
        rp = len(numbers) - 1

        while lp < rp:
            res = numbers[lp] + numbers[rp]
            if res == target:
                return [lp+1, rp+1]

            if res < target:
                lp += 1
            else:
                rp -= 1