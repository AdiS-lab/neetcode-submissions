class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        islands = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    islands += 1
                    q = deque([(i,j)])

                    grid[i][j] = '0'


                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '1':
                                q.append((nx, ny))
                                grid[nx][ny] = '0'

        return islands
        