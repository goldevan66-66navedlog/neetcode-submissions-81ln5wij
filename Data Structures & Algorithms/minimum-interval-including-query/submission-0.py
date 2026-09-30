class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minH = []

        res,i = {}, 0

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                s,e = intervals[i]
                heapq.heappush(minH,[e-s+1,e])
                i+=1
            while(minH and minH[0][1]< q):
                heapq.heappop(minH)
            
            res[q] = minH[0][0] if minH else -1
        
        return [res[q] for q in queries]

        # pos = {q:[i,float("inf")] for i,q in enumerate(queries)}
     
        # intervals.sort()
        # # queries.sort()

        # inter

        # return []

        