class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        rmax = lmax = res = 0 

        # two things that make it work = the subtraction makes sure that 
        # any left value greater than the last will add 0, only lmax will
        # continue adding

        while l < r:
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                res += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                res += rmax - height[r]
                r -= 1
        
        return res