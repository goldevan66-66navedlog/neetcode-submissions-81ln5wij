class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        # for i in range(1,len(coins)):
        #     for j in range(1,amount):
        #         res = 0
        #         if(j%coins[i] == 0):
        #             res += 1
        #         if(j-coins[i]>0):
        #             res += dp[i-1][j-coins[i]]
        
        # return dp[-1][-1]

        # dp = {}
        
        # def dfs(i,a):
        #     if(a > amount):
        #         return 0
        #     if(a == amount):
        #         return 1
        #     if(i == len(coins)):
        #         return 0
        #     if((i,a) in dp):
        #         return dp[(i,a)]
        #     # dp[(i,a)] = 0
        #     # for j in range(i,len(coins)):
        #     dp[(i,a)] = dfs(i,a+coins[i]) + dfs(i+1,a)
        #     return dp[(i,a)]
        
        # return dfs(0,0)

        dp = [0]*(amount+1)
        dp[0] = 1

        for i in range(len(coins)):
            nextDP = [0]*(amount+1)
            nextDP[0] = 1

            for a in range(1,amount+1):
                nextDP[a] += dp[a]

                if(a-coins[i] >= 0):
                    nextDP[a] += nextDP[a-coins[i]]
            dp = nextDP
        
        return dp[amount]

        