class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        res = []

        def dfs(i,curr,total):
            if(total == target):
                res.append(curr.copy())
                return
            if(i>=len(candidates) or total > target):
                return
            else:
                curr.append(candidates[i])

                nxt = i+1
                while(nxt < len(candidates) and candidates[nxt] == candidates[i]):
                    nxt += 1

                dfs(i+1,curr,total+candidates[i])

                curr.pop()

                dfs(nxt,curr,total)
            
        dfs(0,[],0)

        return res