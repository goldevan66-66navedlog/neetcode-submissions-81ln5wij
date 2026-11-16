class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opp = {}

        for i in range(len(nums)):
            if(nums[i] in opp):
                return [opp[nums[i]],i]
            opp[target-nums[i]] = i
        