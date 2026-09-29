"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if(not intervals):
            return 0
        rooms = 1
        na = [[intervals[0].end,intervals[0].start]] #end, start
        heapq.heapify(na)

        intervals.sort(key = lambda i: i.start)

        for i in range(1,len(intervals)):
            if(intervals[i].start>=intervals[i-1].end or intervals[i].end <=intervals[i-1].start):
                # heapq.heappush(na,[intervals[i].end,intervals[i].start])
                continue
            elif(na and intervals[i].start>=na[0][0]):
                heapq.heappop(na)
            else:
                # heapq.heappush(na,[intervals[i].end,intervals[i].start])
                rooms += 1
            heapq.heappush(na,[intervals[i].end,intervals[i].start])
        
        return rooms