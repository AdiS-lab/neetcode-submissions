class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 checks = search row for duplicates
        # traverse diagonally
        # every 3rd so if multiple of 3 then have to check the 3 boxes + the one at 
        
        box1, box2, box3 = set(), set(), set()

        for i in range(9):
            if i == 3 or i == 6:
                box1, box2, box3 = set(), set(), set()

            row = board[i]
            col = [board[r][i] for r in range(9)]
            
            if i == 3:
                print(row)
                print(col)

            row_seen = set()
            col_seen = set()

            for r,c in zip(row, col):
                if r in row_seen or c in col_seen:
                    return False
                if r != '.':
                    row_seen.add(r)
                if c != '.':
                    col_seen.add(c)


            for k in range(3):
                if row[k] in box1 or row[k+3] in box2 or row[k+6] in box3:
                    return False
                
                if row[k] != '.':
                    box1.add(row[k])
                if row[k+3] != '.':
                    box2.add(row[k+3])
                if row[k+2*3] != '.':
                    box3.add(row[k+2*3])

        return True
                
                
