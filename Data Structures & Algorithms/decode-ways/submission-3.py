class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            # if we're at end (for the first) or already have explored
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            
            # increment for the single digit case
            res = dfs(i+1)

            # increment for the double digit case
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)

            dp[i] = res

            return res

        return dfs(0)