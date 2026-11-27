class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            exp = math.floor(math.log2(n))
            print(f"{exp=}")
            n-=2**exp
            count += 1
        
        return count

        