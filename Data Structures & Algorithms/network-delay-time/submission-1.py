class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}

        for v1, v2, e in times:
            adj[v1].append([v2,e])
        
        minHeap = []
        heapq.heappush(minHeap,[0,k])
        total = 0
        visited = set()

        while minHeap:
            d, node = heapq.heappop(minHeap)
            if(node in visited):
                continue

            visited.add(node)

            total = d
            
            for nei in adj[node]:
                v, e = nei
                if(v in visited):
                    continue
                heapq.heappush(minHeap,[e+d,v])

        return total if len(visited) == n else -1

        # def dfs()
        