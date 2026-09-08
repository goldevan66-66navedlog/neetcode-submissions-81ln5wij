class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # self.largest = k
        # for i in range(len(nums)):
        #     nums[i] = nums[i]*-1
        # heapq.heapify(nums)
        # self.data = nums
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while(len(self.minheap)>k):
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        # heapq.heappush(self.data,val*-1)

        # count = 1
        # values = []
        # while(count<=self.largest):
        #     values.append(heapq.heappop(self.data))
        #     count += 1
        
        # res = values[-1]*-1

        # for v in values:
        #     heapq.heappush(self.data,v)
        
        # return res

        heapq.heappush(self.minheap,val)
        if(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]

        
