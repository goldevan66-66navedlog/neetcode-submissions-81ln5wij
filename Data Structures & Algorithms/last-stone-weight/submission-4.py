class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        # print(stones)
        while(len(stones)>1):
            stoneOne = heapq.heappop_max(stones)
            stoneTwo = heapq.heappop_max(stones)
            # print(stoneOne)
            # print(stoneTwo)
            if(stoneOne == stoneTwo):
                continue
            elif(stoneOne < stoneTwo):
                heapq.heappush_max(stones,stoneTwo-stoneOne)
            else:
                heapq.heappush_max(stones,stoneOne-stoneTwo)
        return stones[0] if stones else 0
            
        