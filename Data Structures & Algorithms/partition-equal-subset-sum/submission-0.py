class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if(total%2==1):
            return False
        total = total//2

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            nextDp = set()
            for n in dp:
                nextDp.add(n+nums[i])
                nextDp.add(n)
            dp = nextDp
        return total in dp



        