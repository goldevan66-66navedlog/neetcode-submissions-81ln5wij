class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        
        adj = {i:[] for i in range(n)}

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def dfs(i,prev):
            if(i in visited):
                return True

            visited.add(i)

            for j in adj[i]:
                if(j == prev):
                    continue
                dfs(j,i)
            return True

        res = 0

        for i in range(n):
            if(i not in visited):
                res += 1
                dfs(i,-1)
        
        return res
        