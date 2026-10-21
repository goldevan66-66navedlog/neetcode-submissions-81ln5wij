class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        solutions = set()
        
        poss = []
        def dfs(i): 
            if(i>=len(nums)):
                temp = poss.copy()
                solutions.add(tuple(temp))
            else:
                print(i)
                poss.append(nums[i])

                dfs(i+1)

                poss.pop()
                dfs(i+1)
        
        dfs(0)
        
        return [list(i) for i in solutions]