class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(i,j,k):
            if(k == len(word)):
                return True
            if(i < 0 or j < 0 or i >= ROWS or j >= COLS or board[i][j] != word[k] or board[i][j] == "*"):
                return False
            
            board[i][j] = "*"

            result = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1) or dfs(i,j+1,k+1))

            board[i][j] = word[k]
            return result

        for r in range(ROWS):
            for c in range(COLS):
                if(dfs(r,c,0) == True):
                    return True
        return False

        # return True
        # copy_board = board.copy()
        # def boardy(b,i,j,k):
        #     if(b[i][j] != word[k]):
        #         return False

        #     if(k >= len(word)-1):
        #         return True

        #     b[i][j] = "*"
        #     k += 1

        #     up = [i+1,j] if (i+1>=0 and i+1 < len(b)) else []
        #     down = [i-1,j] if (i-1>=0 and i-1 < len(b)) else []
        #     left = [i,j-1] if (j-1>=0 and j-1 < len(b[i])) else []
        #     right = [i,j+1] if (j+1>=0 and j+1 < len(b[i])) else []
            
        #     direct = [up, down, left, right]
        #     boo = []
        #     for d in direct:
        #         if(d):
        #             ii, jj = d[0], d[1]
        #             boo.append(boardy(b,ii,jj,k))
        #     b[i][j] = word[k-1]
        #     return sum(boo)
        
        # for row in range(len(board)):
        #     for col in range(len(board[row])):
        #         if(boardy(board,row,col,0) == True):
        #             return True
        # return False



            

