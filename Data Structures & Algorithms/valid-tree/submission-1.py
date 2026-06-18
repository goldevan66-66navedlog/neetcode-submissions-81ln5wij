class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if(not n):
            return True
        
        adj = {i:[] for i in range(n)}

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        visited = set()

        def dfs(i,prev):
            if(i in visited):
                return False
            visited.add(i)
            for j in adj[i]:
                if(j == prev):
                    continue
                if(not dfs(j,i)):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n

        # if(len(edges) == n):
        #     return False
        
        # indegree = [0] * n
        # adj = [[] for _ in range(n)]

        # for i,j in edges:
        #     indegree[j] += 1
        #     adj[i].append(j)
        
        # q = deque()
        # for i in range(n):
        #     if(indegree[i] == 0):
        #         q.append(i)
        
        # finish = 0
        # if(len(q) > 1):
        #     return False
        # else:
        #     while q:
        #         node = q.popleft()
        #         finish += 1
        #         for nei in adj[node]:
        #             indegree[nei] -= 1
        #             if(indegree[nei] == 0):
        #                 q.append(nei)
        
        # return True if finish == n else False