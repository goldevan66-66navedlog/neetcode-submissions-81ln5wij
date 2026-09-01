class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        #memoization using recursion
        # dp = {}

        # def dfs(i,a):
        #     if(i == len(nums)):
        #         return 1 if a == target else 0
        #     if((i,a) in dp):
        #         return dp[(i,a)]
        #     dp[(i,a)] = dfs(i+1,a+nums[i]) + dfs(i+1,a-nums[i])
        #     return dp[(i,a)]

        # return dfs(0,0)

        #dp technique with optimized space effiency
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(len(nums)):
            nex_dp = defaultdict(int)
            for sum_c, count in dp.items():
                nex_dp[sum_c-nums[i]] += count
                nex_dp[sum_c+nums[i]] += count
            dp = nex_dp
        
        return dp[target]

