class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # loop through switch off 1s and 0s after visiting
        # and keep going

        r, c = len(grid), len(grid[0])

        q = deque()
        islands = 0
        for i in range(r): 
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    q.append((i, j))
    
                    while q:
                        i, j = q.pop()
                        grid[i][j] = 0

                        if j != 0 and grid[i][j-1] == '1': # left
                            q.append((i, j-1))
                        if j != c-1 and grid[i][j+1] == '1': # right
                            q.append((i, j+1))
                        if i != 0 and grid[i-1][j] =='1': # top
                            q.append((i-1, j))
                        if i != r-1 and grid[i+1][j] == '1': # bottom
                            q.append((i+1, j))

        
        return islands











        
        