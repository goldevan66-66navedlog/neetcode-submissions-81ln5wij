class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0

        while(right > left):
            res = max(res,((right-left)*min(heights[left],heights[right])))
            if(heights[left]>heights[right]):
                right -= 1
            else:
                left += 1
        return res
        