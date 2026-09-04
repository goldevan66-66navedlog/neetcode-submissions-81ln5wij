class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(i,j):
            if(j == len(word2)):
                return len(word1)-1-i
            if(i == len(word1)):
                return 0
            if((i,j) in dp):
                return dp[(i,j)]
            if(word1[i] == word2[j]):
                dp[(i,j)] = dfs(i+1,j+1)
            else:
                res = float("inf")
                res = min(res,1+dfs(i+1,j))
                res = min(res,1+dfs(i,j+1))
                res = min(res,1+dfs(i+1,j+1))
                dp[(i,j)] = res
            return dp[(i,j)]
        return dfs(0,0)+1