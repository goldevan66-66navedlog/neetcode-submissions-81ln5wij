"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res,count = 0,0
        s,e = 0,0

        while(s < len(intervals)):
            if(start[s] < end[e]):
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res,count)
        return res
        # if(not intervals):
        #     return 0
        # rooms = 1
        # na = [[intervals[0].end,intervals[0].start]] #end, start
        # # heapq.heapify(na)

        # intervals.sort(key = lambda i: i.start)

        # for i in range(1,len(intervals)):
        #     if(intervals[i].start>=intervals[i-1].end or intervals[i].end <=intervals[i-1].start):
        #         continue
        #     elif(na and intervals[i].start>=na[0][0]):
        #         heapq.heappop(na)
        #     else:
        #         rooms += 1
        #     heapq.heappush(na,[intervals[i].end,intervals[i].start])
        
        # return rooms