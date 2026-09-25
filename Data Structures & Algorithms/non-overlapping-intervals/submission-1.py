class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: i[0])
        prev = intervals[0]
        delete = 0
        for i in range(1,len(intervals)):
            if(intervals[i][1] <= prev[0]):
                continue
            elif(intervals[i][0] >= prev[1]):
                prev = intervals[i]
                continue
            else:
                if(prev[1] > intervals[i][1]):
                    prev = intervals[i]
                delete += 1
        
        return delete
