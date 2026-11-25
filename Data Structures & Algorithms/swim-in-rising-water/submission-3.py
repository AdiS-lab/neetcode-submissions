class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # r, c, max_height
        N = len(grid)
        visit = set()
        minH = [(grid[0][0], 0, 0)]
        directions = ((1,0), (-1,0), (0,1), (0,-1))
        visit.add((0,0))

        while minH:
            height, x, y = heapq.heappop(minH)

            if x == N -1 and y == N - 1:
                return height

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visit:
                    visit.add((nx, ny))
                    heapq.heappush(minH, (max(height, grid[nx][ny]), nx, ny))                