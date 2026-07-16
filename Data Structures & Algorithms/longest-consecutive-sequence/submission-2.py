class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = set()

        for n in nums:
            d.add(n)
        
        res = 0
        for n in nums:
            if(n-1 not in d):
                start = n
                count = 1
                while(start+count in d):
                    d.remove(start+count)
                    count+= 1

                res = max(res,count)
        
        return res
        
