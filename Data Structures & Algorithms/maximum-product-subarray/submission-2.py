class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax = 1

        res = max(nums)

        for n in nums:
            if(n == 0):
                currMin = 1
                currMax = 1
            else:
                temp = currMax
                currMax = max(n,currMax*n,currMin*n)
                currMin = min(n,temp*n,currMin*n)

                res = max(res,currMax)
        
        return res

        