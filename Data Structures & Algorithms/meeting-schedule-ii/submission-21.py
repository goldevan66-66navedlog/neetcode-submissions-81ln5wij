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

        # the idea here is that when you have a start value check if the meeting ending first out of all the meeting processed so far is less than the start value of the next meeting, if it is then the number of meeting does not change as this starting meeting will take the meeting room of the ending meeting, on the other hand if it is not then they are overlapping so increase the count of rooms, my intution below was process each start time and check if its overlapping if not then continue then check if the current minimum ending time is less than the current start time, if it is then pop the minimum time to say that meeting has ended, if this is not true then the meeting is overlaping so add to the count, regardless of if these condions you will always add the end time to the heap to keep track of the next possible end time which is the minimum. This is elmulated above as we process the start times one by one with the list and if the start time is greater than the least end time then we "pop" for the list or in other words move the end pointer forward. This is the same thing as below but more consise.
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