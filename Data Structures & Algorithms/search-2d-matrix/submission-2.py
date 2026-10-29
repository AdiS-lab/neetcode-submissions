class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search = idea of starting in middle and cutting things in half progressively. so in this case we could start at
        # 3 x 4 so 12 / 2 = 6 
        # if 11 > target
        # find center, and then recalculate based on moving the pointers around
        # 10 = mid

        if not matrix:
            return False

        lenr = len(matrix)
        lenc = len(matrix[0])

        start = 0
        end = lenr * lenc

        while start < end:
            mid_ind = (start + end) // 2 # to move between mid indices

            r = mid_ind // lenc # row
            c = mid_ind % lenc # cols
            # mid index

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                end = mid_ind 
            else:
                start = mid_ind + 1
        
        return False





