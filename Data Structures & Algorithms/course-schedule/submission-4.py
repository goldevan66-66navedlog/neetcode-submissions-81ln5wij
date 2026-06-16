# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.children = {}
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        q = deque()

        for i in range(numCourses):
            if(indegree[i] == 0):
                q.append(i)

        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    q.append(nei)
        
        return finish == numCourses

        # preHash = {i:[] for i in range(numCourses)} #creats an adjacency list

        # # populates the adj list
        # for crs, pre in prerequisites:
        #     preHash[crs].append(pre)
        
        # #Keeps track of visited nodes to detect cycles
        # visited = set()

        # # Runs dfs on the node to detect for cycles and explore if this is a valid path
        # def dfs(crs):
        #     if(crs in visited): #means that there exist a loop
        #         return False
        #     if(preHash[crs] == []): # has not prereq so can take whenever or signifies is a valid course that can be taken
        #         return True
            
        #     # adds the node to the visited list to help test for cycles
        #     visited.add(crs)

        #     for pre in preHash[crs]:
        #         if(not dfs(pre)): # if one course is bad, then all coures are bad
        #             return False

        #     visited.remove(crs) #removes the crs from the visted list b/c done traversing the node
        #     preHash[crs] = [] # if the code reaches this point then the node is valid so populate with an empty list
        #     return True
        
        # # run through all nodes as the graph is not necessiarily connected
        # for i in range(numCourses):
        #     if(not dfs(i)): # will turn false if any are false
        #         return False
        # return True




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