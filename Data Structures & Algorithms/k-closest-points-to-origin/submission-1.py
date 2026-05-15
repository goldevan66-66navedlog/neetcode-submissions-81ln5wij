class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for p in points:
            distance = math.sqrt(((p[0]-0)**2)+((p[1]-0)**2))
            heapq.heappush(minheap,(-1*distance,p))
            if(len(minheap)>k):
                heapq.heappop(minheap)
        
        return [k[1] for k in minheap]
        
        