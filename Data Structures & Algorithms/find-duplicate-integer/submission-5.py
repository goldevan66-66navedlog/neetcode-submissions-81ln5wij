class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hshmp = {}

        # for n in nums:
        #     if(n in hshmp):
        #         return n
        #     hshmp[n] = 1

        # # expect = int((1+len(nums)) * len(nums) / 2)
        # # actual = sum(nums)
        # # print(actual)
        # # print(expect)
        # # return expect - actual
        slow, fast = 0,0

        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break

        slow2 = 0

        while(True):
            slow = nums[slow]
            slow2 = nums[slow2]
            if(slow == slow2):
                return slow
        
        