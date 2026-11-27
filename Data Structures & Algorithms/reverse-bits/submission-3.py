class Solution:
    def reverseBits(self, n: int) -> int:
        print(f"{n=}")

        num = 0
        for i in range(32):
            place = 2**i
            exists = n & place
            if exists:
                print(f"{exists=}")
                num += 2 ** (31 - i)
                print(f"{num=}")

        
        return num
        