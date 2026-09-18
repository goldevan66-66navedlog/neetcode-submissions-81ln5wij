class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = float("inf")
        while(l<=r):
            m = l + (r-l)//2
            print(m)
            res = min(res,nums[m])

            if(nums[l]<nums[m] and nums[m]<nums[r]):
                r = m-1
            elif(nums[l]>nums[m]):
                r = m-1
            else:
                l = m+1
        
        return res

