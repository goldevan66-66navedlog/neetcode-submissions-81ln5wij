class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hshmp = {}

        for n in nums:
            if(n in hshmp):
                return n
            hshmp[n] = 1

        # expect = int((1+len(nums)) * len(nums) / 2)
        # actual = sum(nums)
        # print(actual)
        # print(expect)
        # return expect - actual
        
        