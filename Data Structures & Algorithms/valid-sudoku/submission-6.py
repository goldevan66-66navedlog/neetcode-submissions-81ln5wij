class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            col = set()
            box = set()
            for j in range(len(board)):
                r = board[i][j]
                c = board[j][i]
                s = board[(i//3)*3+j%3][(i%3)*3+j//3]
                if((r in row) or (c in col) or (s in box)):
                    return False
                if(r != "."):
                    row.add(r)
                if(c != "."):
                    col.add(c)
                if(s != "."):
                    box.add(s)
        return True

