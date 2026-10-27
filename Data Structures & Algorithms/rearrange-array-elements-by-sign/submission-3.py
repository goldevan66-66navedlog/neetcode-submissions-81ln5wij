class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0
        sign = 1
        array = []

        while(r<len(nums)):
            # searching for the next positive number
            while(r < len(nums)-1 and nums[r]*sign < 0):
                r += 1
            # array.append(nums[r])
            nums = nums[:l] + [nums[r]] + nums[l:r] + nums[r+1:]
            sign *=-1
            l+=1
            r = l
        
        return nums
            
            # once the next positive number is found swap the numbers at index
            # left and right and move left up one and change the sign
            
