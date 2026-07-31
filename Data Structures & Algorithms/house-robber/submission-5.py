class Solution:
    def rob(self, nums: List[int]) -> int:

        # nums = [0] + nums 
        for i in range(len(nums)):
            if(i == 0):
                continue
            elif(i==1):
                nums[i] = max(nums[i],nums[i-1])
            else: 
            # if(nums[i]+nums[i-2] > nums[i-1]):
                nums[i] = max(nums[i]+nums[i-2],nums[i-1])

        return nums[-1]
        


        