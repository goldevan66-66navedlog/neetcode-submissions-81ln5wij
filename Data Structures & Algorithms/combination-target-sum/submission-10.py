class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        solutions = set()

        ps = []

        def dfs(i,s):
            if(i >= len(nums) or s >= target):
                if(s == target):
                    temp = ps.copy()
                    solutions.add(tuple(temp))
            else:
                ps.append(nums[i])
                dfs(i,s+nums[i])

                ps.pop()
                dfs(i+1,s)
        
        dfs(0,0)

        return [list(i) for i in solutions]