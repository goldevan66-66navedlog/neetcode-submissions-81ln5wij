class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partion = []
        
        def dfs(i):
            if(i >= len(s)):
                res.append(partion.copy())
                return
            
            for j in range(i,len(s)):
                if(self.isPalin(s,i,j)):
                    partion.append(s[i:j+1])
                    dfs(j+1)
                    partion.pop()
        
        dfs(0)
        return res
    
    def isPalin(self,s,l,r):
        while(l < r):
            if(s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True
