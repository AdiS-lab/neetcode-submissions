class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # an area surrounded by x's constitutes a region that is surrounded replace. 
        # can't change immediately
        # if hits edge then a bool should flip 

        r, c = len(board), len(board[0])
        seen = set()

        for i in range(r):
            for j in range(c):
                convert = True
                if board[i][j] == "O" and (i,j) not in seen:
                    q = deque([(i, j)])
                    directions = ((1,0), (-1,0), (0,1), (0,-1))
                    region = [(i,j)]
                    seen.add((i,j))

                    while q: 
                        x, y = q.popleft()
                        if x == r - 1 or x == 0 or y == 0 or y == c - 1:
                            convert = False

                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in seen and board[nx][ny] == 'O':
                                q.append((nx, ny))
                                seen.add((nx, ny))
                                region.append((nx, ny))
                    if convert:
                        for v in region:
                            board[v[0]][v[1]] = 'X'
