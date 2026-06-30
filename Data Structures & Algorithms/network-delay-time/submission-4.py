class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # shortest-path-algo:
        # get an adjency list, then add the starting node to the heap
        # set up a bfs to pop from the heap
        # if the node is already in the visited set then continue as don't need to revisit
        # if not, then add the node to the visited set and set the time equal to the weight popped
        # run bfs, getting every node connected to it and push to the heap
        # when pushing to the heap add the time it took to get the the parent node of the current node being added
        # plus the time from the parent to the current node to be the total time to reach that node
        # return the time t only if all nodes have been visted which is represented if the length of the 
        # visited set is equal to n, else return -1 as this is a disconnected graph
        # this runs in E*logv for each edge we have to pop from the heap which take logv time
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append([v,w])
        
        minH = [[0,k]]
        visited = set()
        t = 0

        while minH:
            w1, n1 = heapq.heappop(minH)

            if(n1 in visited):
                continue
            
            visited.add(n1)
            t = w1

            for n2, w2 in adj[n1]:
                if(n2 not in visited):
                    heapq.heappush(minH,[w2+w1,n2])

        return t if len(visited) == n else -1
        
        # adj = {i:[] for i in range(1,n+1)}

        # for v1, v2, e in times:
        #     adj[v1].append([v2,e])
        
        # minHeap = []
        # heapq.heappush(minHeap,[0,k])
        # total = 0
        # visited = set()

        # while minHeap:
        #     d, node = heapq.heappop(minHeap)
        #     if(node in visited):
        #         continue

        #     visited.add(node)

        #     total = d
            
        #     for nei in adj[node]:
        #         v, e = nei
        #         if(v in visited):
        #             continue
        #         heapq.heappush(minHeap,[e+d,v])

        # return total if len(visited) == n else -1

        # def dfs()
        