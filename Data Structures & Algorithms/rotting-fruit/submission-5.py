class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # count = -1 solves 
        # find all 2s before anything, and add to queue
        # 

        r, c = len(grid), len(grid[0])
        q = deque()
        num_ones = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    num_ones += 1

                if grid[i][j] == 2:
                    q.append((i,j))
        count = -1

        while q:
            for i in range(len(q)): # it has to be full layer so full current length
                x, y = q.popleft()
                directions = ((1,0), (-1,0), (0,1), (0,-1))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy # is this how you reference tuples not sure
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                        num_ones -= 1
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            count += 1
            
        if num_ones:
            return -1

        return max(count, 0) 

        