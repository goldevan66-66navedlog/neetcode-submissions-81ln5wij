class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i,curr,total):
            if(total == target):
                res.append(curr.copy())
                return
            if(i >= len(candidates) or total > target):
                return
            
            #inlcude the current element
            curr.append(candidates[i])
            dfs(i+1,curr,total+candidates[i])
            curr.pop()

            #Only include the next unique elemnt that is not equal to the first
            while(i+1<len(candidates) and candidates[i] == candidates[i+1]):
                i+=1
            if(i+1<len(candidates) and candidates[i+1]+total <= target):
                dfs(i+1,curr,total)

        dfs(0,[],0)
        return res
        # res = set()
        # candidates = sorted(candidates)

        # def dfs(i,curr,total):
        #     if(total == target and tuple(curr.copy()) not in res):
        #         res.add(tuple(curr.copy()))
        #         return
        #     if(i >= len(candidates) or total > target):
        #         return
        #     curr += [candidates[i]]
        #     dfs(i+1,curr,total+candidates[i])

        #     last = curr.pop()

        #     n = 1
        #     while( (i+n)<len(candidates) and candidates[i+n] == last):
        #         n += 1
        #     if((i+n)<len(candidates) and candidates[i+n]+total <= target):
        #         dfs(i+n,curr,total)
        
        # dfs(0,[],0)
        # return [list(lst) for lst in res]