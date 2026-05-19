class MedianFinder:

    def __init__(self):

        self.small = [] # max-heap for the smaller values, this pushes the values from the left inward toward the middle
        # -1,-2,-4 -> -4 is the smallest value from the small side wich is closest to the middle as is a max heap by default with negative values
        self.large = [] # min-heap for the large values, this pushes the larger values form the right side towards the middle
        # 5, 6, 8 -> 5 is the smallest value from the large side wich is closer to the middle than the subsequnt larger values
        

    def addNum(self, num: int) -> None:
        # push to the large heap for elements bigger than the min value of the large side else push to the small
        if(self.large and num > self.large[0]):
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,num*-1)
        
        #if uneven move the top value from the uneven to the other heap
        if(len(self.small) > len(self.large)+1):
            val = heapq.heappop(self.small)*-1
            heapq.heappush(self.large,val)
        if(len(self.large) > len(self.small)+1):
            val = heapq.heappop(self.large)*-1
            heapq.heappush(self.small,val)

    def findMedian(self) -> float:
        #if odd number of values, then take the larger lists top value else get their average
        if(len(self.small)>len(self.large)):
            return self.small[0]*-1
        if(len(self.large)>len(self.small)):
            return self.large[0]
        return (self.small[0]*-1+self.large[0])/2
        
        