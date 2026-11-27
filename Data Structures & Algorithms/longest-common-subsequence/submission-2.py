class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        L1 = len(text1)
        L2 = len(text2)

        dp = [[0] * (L2+1) for _ in range(L1+ 1)]
        print(f"{dp}")

        for i in range(L1 -1, -1, -1):
            for j in range(L2-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])

        return dp[0][0]




'''

appearance of letter = new start 
vh   

'''
        