class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = left + (right-left)//2
            if((mid-1 < 0 or nums[mid-1]!=nums[mid]) and (mid+1 == len(nums) or nums[mid+1]!=nums[mid])):
                return nums[mid]
            
            leftsize = mid-1 if nums[mid] == nums[mid-1] else mid

            if(leftsize%2):
                right = mid-1
            else:
                left = mid+1


            
