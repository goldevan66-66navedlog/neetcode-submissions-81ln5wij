class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # points = {i:point for i,point in enumerate(points)}
        # visit = set()
        # heap = [[0,0]]
        # cost = 0

        # def distance(x1,y1,x2,y2):
        #     d = abs(x1-x2)+abs(y1-y2)
        #     return d

        # while heap:
        #     if(len(visit) == len(points)):
        #         break
        #     node = heapq.heappop(heap)
        #     while(node[1] in visit):
        #         node = heapq.heappop(heap)
        #     visit.add(node[1])
        #     point = points[node[1]]
        #     cost += node[0]

        #     for k in points.keys():
        #         if(k not in visit):
        #             c = distance(point[0],point[1],points[k][0],points[k][1])
        #             heapq.heappush(heap,[c,k])
        # return cost

        # cost = {tuple(p):[] for p in points}

        # for i in range(len(points)):
        #     x1, y1 = points[i][0], points[i][1]
        #     for j in range(i+1,len(points)):
        #         x2, y2 = points[j][0], points[j][1]
        #         distance = abs(x1-x2)+abs(y1-y2)
        #         cost[tuple([x1,y1])].append([distance,[x2,y2]])
        
        # for k in cost.keys():
        #     cost[k] = sorted(cost[k])
        
        # print(cost)
        # return 1

        # def cost(x1,y1,x2,y2):
        #     distance = abs(x1-x2)+abs(y1-y2)
        #     return distance
        
        # res = 0
        # while(points):
        #     x1,y1 = points.pop()
        #     m = float("inf") if points else 0
        #     for i in range(len(points)-1):
        #         x2, y2 = points[i][0], points[i][1]
        #         m = min(m,cost(x1,y1,x2,y2))
        #     print(points)
        #     res += m
        # return res

        points = {i:p for i,p in enumerate(points)}
        visited = set()
        heap = [[0,0]]
        res = 0

        while(len(visited)<len(points)):
            p = heapq.heappop(heap)
            while(p[1] in visited):
                p = heapq.heappop(heap)
            node = points[p[1]]
            visited.add(p[1])
            res += p[0]
            for i in range(len(points)):
                if(i not in visited):
                    cost = abs(node[0]-points[i][0]) + abs(node[1]-points[i][1])
                    heapq.heappush(heap,[cost,i])
        return res
    
