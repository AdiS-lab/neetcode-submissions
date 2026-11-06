class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # has to be a way to only search zeroes


        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if not grid[i][j]: # if 0 then began defining distances
                    q = deque([(i, j, 1)]) 

                    while q: # change conditional
                        x, y, count = q.popleft()
                        # within bounds, non negative, and greater than count

                        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != -1 and grid[nx][ny] > count:
                                grid[nx][ny] = count
                                q.append((nx, ny, count + 1))        
        return None
