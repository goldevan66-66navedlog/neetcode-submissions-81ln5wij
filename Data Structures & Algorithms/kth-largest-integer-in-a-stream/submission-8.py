class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.largest = k
        for i in range(len(nums)):
            nums[i] = nums[i]*-1
        heapq.heapify(nums)
        self.data = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.data,val*-1)

        count = 1
        values = []
        while(count<=self.largest):
            values.append(heapq.heappop(self.data))
            count += 1
        
        res = values[-1]*-1

        for v in values:
            heapq.heappush(self.data,v)
        
        return res

        
