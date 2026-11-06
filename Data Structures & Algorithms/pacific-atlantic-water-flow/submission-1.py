class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        r, c = len(heights), len(heights[0])

        def bfs(arr):
            seen = set(arr)
            q = deque(arr)
            while q:
                x, y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < r and 0 <= ny < c 
                    and (nx, ny) not in seen 
                    and heights[nx][ny] >= heights[x][y]): 
                        seen.add((nx, ny))
                        q.append((nx, ny))
            return seen

        PACIFIC = bfs([(i,0) for i in range(r)] + [(0,j) for j in range(c)])
        ATLANTIC = bfs([(i,c-1) for i in range(r)] + [(r-1,j) for j in range(c)])

        return [list(p) for p in PACIFIC & ATLANTIC]