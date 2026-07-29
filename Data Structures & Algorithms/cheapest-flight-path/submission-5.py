class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = {i:float("inf") for i in range(n)}
        price[src] = 0

        for i in range(k+1):
            temp = price.copy()
            for s,d,p in flights:
                if(price[s] == float("inf")):
                    continue
                if(price[s]+p < temp[d]):
                    temp[d] = price[s]+p
            price = temp
        
        return -1 if price[dst] == float("inf") else price[dst]

        # adj = {i:[] for i in range(n)}
        # visited= set()
        
        # for s,d,p in flights:
        #     adj[s].append([d,p])
        
        # heap = []
        # for d,p in adj[src]:
        #     heapq.heappush(heap,[p,d,1])
        
        # res = []
        # while heap:
        #     p,d,stops = heapq.heappop(heap)
        #     if(stops > k):
        #         continue
        #     if(d == dst):
        #         res.append(p)

        #     if(d in visited):
        #         break

        #     for cd,cp in adj[d]:
        #         heapq.heappush(heap,[p+cp,cd,stops+1])
        
        # return min(res) if res else -1