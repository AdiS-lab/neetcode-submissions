class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.countOnes(i) for i in range(n + 1)]

    def countOnes(self, num):
        count = 0
        while num > 0:
            exp = math.floor(math.log2(num))
            num -= 2 ** exp
            count += 1
        return count
        