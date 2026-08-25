class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    dp[i] = max(dp[i],dp[j]+1)
        
        return max(dp)
        # # currmin = nums[0]
        # # currmax = nums[0]

        # dp = [0] * len(nums)
        # dp[0] = 1
        # seen = set()
        # seen.add(nums[0])

        # for i in range(len(nums)):
        #     print(nums[i])
        #     for j in range(i,len(nums)):
        #         if(nums[i] >= nums[j]):
        #             dp[j] = dp[i]
        #         else:
        #             dp[j] = dp[i] + 1
        #         print(dp)
        # return max(dp)
                