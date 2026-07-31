class Solution:
    def rob(self, nums: List[int]) -> int:
        flag = False
         
        if(len(nums)<4):
            return max(nums)

        temp1 = nums[:-1]
        temp2 = nums[1:]

        return max(self.robi(temp1),self.robi(temp2))

    def robi(self, arr):
        one, two = 0,0
        for i in range(len(arr)):
            temp = max(arr[i]+one,two)
            one = two
            two = temp
        return two
                

        