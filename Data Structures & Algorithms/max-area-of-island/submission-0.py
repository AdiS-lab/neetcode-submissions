class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        r, c = len(grid), len(grid[0])
        maxArea = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    q = deque([(i,j)])
                    tempArea = 1
                    grid[i][j] = 0 

                    while q:
                        x, y = q.popleft()
                        for dx, dy in ((0,1),(0,-1) ,(1,0),(-1,0)):
                            nx, ny  = x + dx, y + dy
                            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny]:
                                q.append((nx, ny))
                                grid[nx][ny] = 0
                                tempArea += 1

                    maxArea = max(maxArea, tempArea)

        return maxArea