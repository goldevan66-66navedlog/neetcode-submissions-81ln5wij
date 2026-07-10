class Solution:
    import math
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res += [math.prod(nums[:i]+nums[i+1:])]
        return res
