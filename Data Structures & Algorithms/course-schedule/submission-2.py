# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.children = {}
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preHash = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preHash[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if(crs in visited): #means that there exist a loop
                return False
            if(preHash[crs] == []):
                return True
            visited.add(crs)

            for pre in preHash[crs]:
                if(not dfs(pre)):
                    return False

            visited.remove(crs)
            preHash[crs] = []
            return True
        
        for i in range(numCourses):
            if(not dfs(i)):
                return False
        return True
        # nodes = Node()

        # for l in prerequisites:
        #     a,b = l
        #     nodes[b] = a
        
        # visited = set()
        # for k in nodes.keys():
        #     print(visited)
        #     if(k in visited or numCourses < 0):
        #         return False
        #     visited.add(nodes[k])
        #     numCourses -= 1
        
        # return True