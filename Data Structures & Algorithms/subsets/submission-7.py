class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        solutions = set()
        
        poss = []
        def dfs(i): 
            if(i>=len(nums)):
                temp = poss.copy()
                solutions.add(tuple(temp))
            else:

                # you can either have the number index i
                poss.append(nums[i])

                dfs(i+1)
                
                # or not have the number at index i
                poss.pop()
                dfs(i+1)
        
        dfs(0)
        
        return [list(i) for i in solutions]