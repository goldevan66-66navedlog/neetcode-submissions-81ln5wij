class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        
        res = [0]*len(nums)

        for i in range(len(nums)):
            prefix[i] = prefix[i-1]*nums[i]
            suffix[len(nums)-1-i] = nums[-1-i]*suffix[-i]
        
        
        for i in range(len(nums)):
            if(i-1 not in range(len(nums))):
                res[i] = suffix[i+1]
            elif(i+1 not in range(len(nums))):
                res[i] = prefix[i-1]
            else:
                res[i] = prefix[i-1]* suffix[i+1]

        return res
