class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currmax = 1
        currmin = 1

        for n in nums:
            if(n == 0):
                currmax = 1
                currmin = 1
                continue
            temp = currmax
            currmax = max(currmax*n,n,currmin*n)
            currmin = min(temp*n,n,currmin*n) 
            res = max(res,currmax)
        
        return res