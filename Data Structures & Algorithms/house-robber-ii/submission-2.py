class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.rob2(nums[1:]),self.rob2(nums[:-1]))
    
    def rob2(self, nums):
        num1, num2 = 0,0

        for n in nums:
            temp = max(n+num1,num2)
            num1 = num2
            num2 = temp
        return num2