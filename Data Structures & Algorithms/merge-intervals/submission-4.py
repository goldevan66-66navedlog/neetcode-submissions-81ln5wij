class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key = lambda i: i[0])
        # newInterval = intervals[0]
        # res = []

        # for i in range(len(intervals)):
        #     if(newInterval[1] < intervals[i][0]):
        #         res.append(newInterval)
        #         newInterval = intervals[i]
        #     elif(newInterval[0] > intervals[i][1]):
        #         res.append(intervals[i])
        #     else:
        #         newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        
        # res.append(newInterval)
        # return res

        intervals.sort(key = lambda i: i[0])

        res = []
        res.append(intervals[0])

        for i in range(len(intervals)):
            if(res[-1][1] < intervals[i][0]):
                res.append(intervals[i])
            elif(res[-1][0] > intervals[i][1]):
                res.append(intervals[i])
            else:
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1],intervals[i][1])]
           
        
        return res

