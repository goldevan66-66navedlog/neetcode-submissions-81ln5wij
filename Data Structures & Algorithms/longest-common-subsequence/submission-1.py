class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #text2 are the columns and text1 is the rows
        # dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        # for i in range(len(text1)-1,-1,-1):
        #     for j in range(len(text2)-1,-1,-1):
        #         if(text1[i] == text2[j]):
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        # return dp[0][0]

        if(len(text1)>len(text2)):
            text1,text2 = text2,text1
        
        prev = [0]*(len(text1)+1)
        nex = [0]*(len(text1)+1)

        for i in range(len(text2)-1,-1,-1):
            for j in range(len(text1)-1,-1,-1):
                if(text1[j] == text2[i]):
                    nex[j] = 1 + prev[j+1]
                else:
                    nex[j] = max(nex[j+1],prev[j])
            prev = nex
            nex = [0]*(len(text1)+1)
        
        return prev[0]
