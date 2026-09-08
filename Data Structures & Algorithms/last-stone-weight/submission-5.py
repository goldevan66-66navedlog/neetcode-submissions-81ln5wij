class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for s in stones:
            maxheap.append(s*-1)
        heapq.heapify(maxheap)

        while(len(maxheap)>1):
            stone1 = heapq.heappop(maxheap)
            stone2 = heapq.heappop(maxheap)

            if(stone1 == stone2):
                continue
            if(stone1 < stone2):
                heapq.heappush(maxheap,stone1-stone2)
            else:
                heapq.heappush(maxheap,stone2-stone1)
        
        return 0 if not maxheap else maxheap[-1]*-1