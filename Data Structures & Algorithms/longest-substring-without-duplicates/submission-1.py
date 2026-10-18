class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # "zxyzxyz"

        # xyzzxy
        
        # "xxxx"

        # max_length and search by that window
        
        seen = set()
        lp = 0 
        max_len = 0 

        for rp in range(len(s)):
            while s[rp] in seen:
                seen.remove(s[lp])
                lp += 1

            seen.add(s[rp])
            max_len = max(max_len, rp - lp + 1)

        return max_len 

        # idea is when hitting duplicate then increment left pointer until it is at z
        
        