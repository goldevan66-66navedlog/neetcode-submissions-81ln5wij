class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp = {}

        # def dfs(i,j):
        #     if(j == len(word2)):
        #         return len(word1)-i
        #     if(i == len(word1)):
        #         return len(word2)-j
        #     if((i,j) in dp):
        #         return dp[(i,j)]
        #     if(word1[i] == word2[j]):
        #         dp[(i,j)] = dfs(i+1,j+1)
        #     else:
        #         res = float("inf")
        #         res = min(res,1+dfs(i+1,j))
        #         res = min(res,1+dfs(i,j+1))
        #         res = min(res,1+dfs(i+1,j+1))
        #         dp[(i,j)] = res
        #     return dp[(i,j)]
        # return dfs(0,0)

        # dp = [[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        # for i in range(len(word1)):
        #     dp[-1][i] = len(word1)-i
        # for j in range(len(word2)):
        #     dp[j][-1] = len(word2)-j
        
        # for i in range(len(word2)-1,-1,-1):
        #     for j in range(len(word1)-1,-1,-1):
        #         mini = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])
        #         dp[i][j] = (mini+1 if word1[j] != word2[i] else dp[i+1][j+1])
        
        # return dp[0][0]

        if(len(word1) < len(word2)):
            dp = [i for i in range(len(word1),-1,-1)]
        else:
            dp = [i for i in range(len(word2),-1,-1)]
            word1, word2 = word2, word1
        count = 1
        for i in range(len(word2)-1,-1,-1):
            new = [0]*(len(word1)+1)
            new[-1] = count
            count += 1
            for j in range(len(word1)-1,-1,-1):
                new[j] = 1 + min(new[j+1], dp[j], dp[j+1]) if word2[i] != word1[j] else dp[j+1]
            dp = new
        
        return dp[0]