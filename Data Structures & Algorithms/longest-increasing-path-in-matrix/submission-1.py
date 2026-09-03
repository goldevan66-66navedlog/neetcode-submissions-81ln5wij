class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {} # (i,)
        moves = [[0,1],[0,-1],[-1,0],[1,0]]
        # up=1, down=2, right =3, left=4

        def dfs(i,j,prev):
            if(i not in range(len(matrix)) or j not in range(len(matrix[0])) or matrix[i][j]<=prev):
                return 0
            if((i,j) in dp):
                return dp[(i,j)]
            res = 1
            for di, dj in moves:
                res = max(res,1+dfs(di+i,dj+j,matrix[i][j]))
            dp[(i,j)] = res
        
            return dp[(i,j)]
        
        resl = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                resl = max(resl,dfs(i,j,-1))
        return resl