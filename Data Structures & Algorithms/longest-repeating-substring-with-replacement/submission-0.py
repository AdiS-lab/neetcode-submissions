class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        frequency = {}
        max_frequency = 0
        lp = 0
        max_len = 0

        for rp in range(len(s)):
            frequency[s[rp]] = frequency.get(s[rp], 0) + 1
            max_frequency = max(max_frequency, frequency[s[rp]])

            # window_size - most_common > k means too many replacements needed
            while (rp - lp + 1) - max_frequency > k:
                frequency[s[lp]] -= 1    # you had `- 1` instead of `-= 1`
                lp += 1

            max_len = max(max_len, rp - lp + 1)

        return max_len    # return window size, not max_frequency

            # B FREQ > 1, so have to increment something
        
        

        