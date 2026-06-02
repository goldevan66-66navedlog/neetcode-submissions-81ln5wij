class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pd = set()
        nd = set()
        res = []

        board = [["."]*n for _ in range(n)]

        def dfs(i):
            if(i == n):
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if((c in cols) or (i-c in nd) or (i+c in pd)):
                    continue
                cols.add(c)
                nd.add(i-c)
                pd.add(i+c)
                board[i][c] = "Q"
                
                dfs(i+1)
                cols.remove(c)
                nd.remove(i-c)
                pd.remove(i+c)
                board[i][c] = "."
            return
        dfs(0)
        return res

        # board = [["."]*n for _ in range(n)]
        # res = []
        # def dfs(i,j,c,dn,dp):
        #     board[i][j] = "Q"
        #     if(i >= n-1):
        #         res.append(["".join(k) for k in board])
        #         board[i][j] = "."
        #         return

        #     c.add(j)
        #     dn.add(i-j)
        #     dp.add(i+j)
        #     for k in range(n):
        #         if(abs(k-j)>=2 and (k not in c) and (i-k not in dn) and (i+k not in dp)):
        #             print(f'i: {i} and j: {k}')
        #             dfs(i+1,k,c,dn,dp)
        #     board[i][j] = "."
        #     c.remove(j)
        #     dn.remove(i-j)
        #     dp.remove(i+j)
        #     return
        # ans = []
        # for p in range(n):
        #     dfs(0,p,set(),set(),set())

        # return res