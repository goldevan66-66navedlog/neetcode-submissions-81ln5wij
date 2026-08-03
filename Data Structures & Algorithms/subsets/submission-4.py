class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()

        sub = []
        def dfs(i):
            if i == len(nums):
                return
            curr = sub
            curr.append(nums[i])
            res.add(tuple(curr.copy()))
            dfs(i+1)

            curr.pop()
            res.add(tuple(curr.copy()))
            dfs(i+1)
        
        dfs(0)
        return [list(i) for i in res]
