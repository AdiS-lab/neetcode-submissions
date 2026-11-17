class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        resLen, resIdx = 0, 0

        # create dp square row len = n, col len = n
        dp = [[False] * n for _ in range(n)] 

        # iterate from top right middle
        # each iteration will go mid out to right (build the diagonals)

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # dp check, basically 2 conditions
                # 1. if both sides are equal + only one letter in between True
                # 2. if both sides are equal + the palindrome inside then True
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                
                    if (j - i + 1) >= resLen:
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]