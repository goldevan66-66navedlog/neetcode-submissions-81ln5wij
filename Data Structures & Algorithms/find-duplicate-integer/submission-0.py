class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hshmp = {}

        for n in nums:
            if(n in hshmp):
                return n
            hshmp[n] = 1
        
        