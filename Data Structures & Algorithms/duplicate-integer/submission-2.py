class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valid = set()

        for n in nums:
            if(n in valid):
                return True
            valid.add(n)
        
        return False