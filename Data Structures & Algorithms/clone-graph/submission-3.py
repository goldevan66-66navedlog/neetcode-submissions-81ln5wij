"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(n):
            if n in clone:
                return clone[n]
            copy = Node(n.val)
            clone[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        
        return dfs(node) if node else None
        # visited = set()
        # copy = {}
        # def dfs(n):
        #     if(not n.neighbors or n in visited):
        #         return
        #     visited.add(n)
        #     print(n.val)
        #     if(n not in copy):
        #         copy[n] = Node(n.val)
        #     for nei in n.neighbors:
        #         # visited.add(nei)
        #         dfs(nei)
        #         if(nei not in copy):
        #             copy[nei] = Node(nei.val)
        #         copy[n].neighbors.append(copy[nei])
        # dfs(node)
        # # dfs(copy[node])
        # # print(copy[node])
        # print(copy)


        # return node
        