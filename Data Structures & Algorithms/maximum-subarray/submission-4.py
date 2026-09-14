class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxA = nums[0]
        cs = 0

        for i in range(len(nums)):
            if(cs < 0):
                cs = 0
            cs += nums[i]
            maxA = max(maxA,cs)
        
        return maxA