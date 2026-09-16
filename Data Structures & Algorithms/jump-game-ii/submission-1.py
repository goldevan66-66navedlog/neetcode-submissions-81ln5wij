class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while(r < len(nums)-1):
            far = 0
            for i in range(l,r+1):
                far = max(far,i+nums[i])
            l = r+1
            r = far
            res+=1
        
        return res
        # goal = len(nums)-1
        # jumps = 0
        
        # for i in range(len(nums)-2,-1,-1):
        #     if(nums[i]+i >= goal):
        #         jumps += 1-(nums[i]+i-goal)
        #         goal = i
        
        # return jumps
        jumps = 0
        goal = 0
        while(goal<len(nums)-1):
            jumps += 1
            goal
        for n in nums:
            jumps += 1
            if(goal+n >= len(nums)-1):
                return jumps
            else:
                goal += n
        return jumps