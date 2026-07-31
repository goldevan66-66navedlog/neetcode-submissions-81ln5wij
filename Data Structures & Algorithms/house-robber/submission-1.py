class Solution:
    def rob(self, nums: List[int]) -> int:

        nums = [0] + nums 
        for i in range(len(nums)):
            if(i < 3):
                continue
            # if(nums[i]+nums[i-2] > nums[i-1]):
            nums[i] = max(nums[i]+nums[i-2],nums[i-1],nums[i]+nums[i-3])

        return max(nums[-1],nums[-2]) if len(nums)>2 else nums[-1]
        


        