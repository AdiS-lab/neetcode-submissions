class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = {}
        for i in range(len(nums)):
            curr = nums[i]
            greater = nums[i]+1
            lower = nums[i]-1

            if curr in check: 
                continue

            elif greater in check and lower in check:
                resArr = check[lower] + [curr] + check[greater]
                check[resArr[0]] = resArr 
                check[resArr[-1]] = resArr
                check[curr] = [curr]

            elif lower in check:
                resArr = check[lower]
                resArr.append(curr)
                check[lower] = resArr
                check[curr] = resArr

            elif greater in check:
                resArr = check[greater]
                resArr.insert(0, nums[i])
                check[greater] = resArr
                check[curr] = resArr

            else:
                check[curr] = [curr]
        maxVal = 0
        for x in list(check.values()):
            if len(x) > maxVal:
                maxVal = len(x)

        return maxVal

        