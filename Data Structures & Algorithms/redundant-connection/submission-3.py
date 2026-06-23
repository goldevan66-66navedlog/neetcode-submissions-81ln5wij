class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)

        def find(n1):
            if(n1 != par[n1]):
                par[n1] = find(par[n1]) #path compression
            return par[n1] # when the root nodes parent is itself so reached the root node
        
        def union(n1,n2):
            p1, p2 = find(n1), find(n2)

            if(p1 == p2): #means that they have already been connected at some point so this edge creates the cycle
                return False
            
            if(rank[p1] > rank[p2]):
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for v1, v2 in edges: # when the cycle is detected by the untion return false then return this edge
            if(not union(v1,v2)):
                return [v1,v2]

        # adj = {i:[] for i in range(1,len(edges)+1)}

        # for v1, v2 in edges:
        #     adj[v1].append(v2)
        #     adj[v2].append(v1)
        
        # # visited = set()
        # res = []

        # def dfs(i,prev,vis):
        #     if(i in vis):
        #         res.append([prev,i])
        #         return

        #     vis.add(i)

        #     for v in adj[i]:
        #         if(v == prev):
        #             continue
        #         dfs(v,i,vis)
        #     return
        
        # for v1,v2 in edges:
        #     dfs(v2,v1,set())
        
        # print(res)
        # return res[-1]


        