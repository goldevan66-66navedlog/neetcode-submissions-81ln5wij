class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while(right > left):
            if(target == (numbers[right]+numbers[left])):
                return [left+1,right+1]
            elif(target<(numbers[right]+numbers[left])):
                right -= 1
            else:
                left += 1
        
        return [left+1, right+1]