class Solution:
    def jump(self, nums: List[int]) -> int:
        #DP algo with memo
        dp = {}

        def dfs(i):
            if(i in dp):
                return dp[i]
            if(i == len(nums)-1):
                return 0
            if(nums[i]==0):
                return 10000000
            
            end = min(i+nums[i]+1,len(nums))
            res = 1000000
            for j in range(i+1,end):
                res = min(res,1+dfs(j))
            dp[i] = res
            return res
        
        return dfs(0)

        #Greedy Algo
        # res = 0
        # l = r = 0

        # while(r < len(nums)-1):
        #     far = 0
        #     for i in range(l,r+1):
        #         far = max(far,i+nums[i])
        #     l = r+1
        #     r = far
        #     res+=1
        
        # return res
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