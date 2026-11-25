class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        t_start = max(grid[0][0], grid[ROWS-1][COLS-1])
        
        def bfs(t):
            directions = ((1,0), (-1,0), (0,1), (0,-1))
            q = deque()
            visit = set()

            visit.add((0,0))
            q.append((0,0))

            while q:
                x, y = q.popleft()
                if x == ROWS -1 and y == COLS -1:
                    return True

                for dx, dy in directions:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] <= t and (nx, ny) not in visit:
                        q.append((nx, ny))
                        visit.add((nx, ny))


            return False


        
        while True:
            if bfs(t_start):
                return t_start

            t_start += 1