class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while(l<=r):
            m = l + ((r-l)//2)
            print(m)
            if(nums[m]==target):
                return m
            # if(nums[m]>nums[l] and nums[m]<nums[r]):
            #     if(nums[m]>target):
            #         r = m-1
            #     else:
            #         l = m+1
            if(nums[m]>=nums[l]):
                if(target<nums[l] or target > nums[m]):
                    l = m+1
                else:
                    r = m-1
            else:
                if(target>nums[r] or target < nums[m]):
                    r = m-1
                else:
                    l = m+1
            # elif(nums[m]<nums[r] and target > nums[r]):
            #     r = m-1
            # elif(nums[m]<nums[l] and target >= nums[l]):
            #     r=m-1
            # elif(nums[m]>nums[r] and target <= nums[r]):
            #     l = m+1
        
        return -1
