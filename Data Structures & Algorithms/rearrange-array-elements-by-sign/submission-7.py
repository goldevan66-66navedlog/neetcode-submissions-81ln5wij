class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []

        for i in range(len(nums)):
            if(nums[i] > 0):
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        
        res = []
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        
        return res

        # l = 0
        # r = 0
        # sign = 1
        # array = []

        # while(r<len(nums)):
        #     # searching for the next positive number
        #     while(r < len(nums)-1 and nums[r]*sign < 0):
        #         r += 1
        #     # array.append(nums[r])
        #     if(r != l):
        #         nums = nums[:l] + [nums[r]] + nums[l:r] + nums[r+1:]
        #     sign *=-1
        #     l+=1
        #     r = l
        
        # return nums


            
            # once the next positive number is found swap the numbers at index
            # left and right and move left up one and change the sign
            
