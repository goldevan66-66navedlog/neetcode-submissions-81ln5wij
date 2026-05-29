class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums = sorted(nums)

        curr = []
        def dfs(i):
            if(i >= len(nums)):
                res.add(tuple([]))
                return []

            curr.append(nums[i])
            dfs(i+1)

            if(tuple(curr) not in res):
                res.add(tuple(curr.copy()))

            curr.pop()
            while(i+1 < len(nums) and nums[i] == nums[i+1]):
                i+= 1
            dfs(i+1)

            if(tuple(curr) not in res):
                res.add(tuple(curr.copy()))
        
        dfs(0)
        return [list(l) for l in res]
        
