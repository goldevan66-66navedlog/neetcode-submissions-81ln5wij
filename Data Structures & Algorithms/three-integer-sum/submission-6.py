class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            target = nums[i]*-1
            left = i+1
            right = len(nums)-1

            while(right > left):
                if(target == (nums[left]+nums[right])):
                    res.add((nums[i],nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif(target > (nums[left]+nums[right])):
                    left += 1
                else:
                    right -= 1
            
        return [r for r in res]