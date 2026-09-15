class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Neetcodes approach greedy:
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if(i+nums[i] >= goal):
                goal = i

        return True if goal == 0 else False
        # My greedy approach starting at the beginning of the list
        # jump = nums[0]-1
        # i = 1
        # if(nums[0]==0 and len(nums)>1):
        #     return False
        # while(True):
        #     if(i >= len(nums)-1):
        #         return True
        #     jump = max(jump,nums[i])
        #     if(jump<=0):
        #         return False
        #     jump -= 1
        #     i += 1
            
        # jump = nums[0]-1
        # i = 1
        # while(True):
        #     print(i)
        #     if(i >= len(nums)-1):
        #         return True
        #     elif(nums[i]==0 and jump>0 or jump>nums[i]):
        #         i += 1
        #         jump -=1
        #     elif(jump<nums[i]):
        #         jump = nums[i]-1
        #         i += 1
        #     else:
        #         return False
        
        # return False

