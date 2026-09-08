class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x,y in points:
            heapq.heappush(maxheap,[self.eucladian(0,0,x,y)*-1,[x,y]])
        
        while(len(maxheap)>k):
            heapq.heappop(maxheap)
        
        return [y for x,y in maxheap]
    
    def eucladian(self,x1,y1,x2,y2):
        return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)