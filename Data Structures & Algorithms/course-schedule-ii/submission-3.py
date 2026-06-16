class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        
        q = deque()

        for i in range(numCourses):
            if(indegree[i] == 0):
                q.append(i)
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if(indegree[nei] == 0):
                    q.append(nei)
        
        return res if len(res) == numCourses else []

        # preHash = {i:[] for i in range(numCourses)}
        
        # for crs, pre in prerequisites:
        #     preHash[crs].append(pre)

        # visiting = set()
        # courses = []

        # def dfs(crs):
        #     if(crs in visiting):
        #         return False
        #     if(preHash[crs] == []):
        #         courses.append(i)
        #         return True

        #     visiting.add(crs)

        #     for pre in preHash[crs]:
        #         if(not dfs(pre)):
        #             return False
        #     visiting.remove(crs)
        #     preHash[crs] = []
        #     return True
        
        # for i in range(numCourses):
        #     if(not dfs(i)):
        #         return []

        # return courses
        