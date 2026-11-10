class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        islands = 0


        def dfs(x, y):
            if x < 0 or x > r - 1 or y < 0 or y > c - 1 or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

            return

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)

        return islands

