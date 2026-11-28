class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        bottom_row = [0] * (amount + 1)
        bottom_row[0] = 1

        for coin in coins[::-1]:
            cur_row = [0] * (amount + 1)

            for i in range(amount + 1):
                cur_row[i] = bottom_row[i]

                if i - coin >= 0:
                    cur_row[i] += cur_row[i-coin]

            bottom_row = cur_row

        print(f"{bottom_row=}")
        return bottom_row[amount]
                


            
        