class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # equation for area = min(height) * (i - i 0)
        # move pointer if lower height
        # go until you reach the middle
        # moving the tall post garuntees


        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
        
        