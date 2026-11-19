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
        
        count = 0
        for i in range(len(board)):
            countR = 0
            countC = 0
            for j in range(len(board)):
                board[i%3+countR][j%3+countC]
                countR = j%3
                countC = j%3
                print(((i//3)*3+j%3),((i%3)*3+j//3))
                # print(count)
                count += 1
                # print(((i//3)*3+countR),(count//9)*3+j//3)
                # print(((i//3)*3+countR),(j//3)+(count//9)*3)
            print("--------------------")

