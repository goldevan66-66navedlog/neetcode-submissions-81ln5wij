class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l,r):
            if(l>r):
                return 0
            if((l,r) in dp):
                return dp[(l,r)]
            dp[(l,r)] = 0
            for i in range(l,r+1):
                coins = nums[l-1] * nums[i] * nums[r+1]
                coins += dfs(l,i-1) + dfs(i+1,r)
                dp[(l,r)] = max(dp[(l,r)],coins)
            return dp[(l,r)]
        return dfs(1,len(nums)-2)
        # dp = [[0]]

        # def dfs(n):
        #     if i not in range(len(nums)):
        #         return 1
        #     if(n in dp):
        #         return dp[nums]
        #     dp[nums] = max(dfs(i+1), dfs())

        # seen = set()??
        # res = 0
        # while nums:
        #     index = 0
        #     mini = nums[index]
        #     for i,n in enumerate(nums):
        #         if(n<mini):
        #             index = i
        #             mini = n
        #     left = 1 if index-1 not in range(len(nums)) else nums[index-1]
        #     middle = nums[index]
        #     right = 1 if index+1 not in range(len(nums)) else nums[index+1]
        #     res += left*middle*right
        #     nums = nums[:index]+nums[index+1:]
        # return res