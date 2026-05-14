class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        while(len(self.minheap)>k):
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if(len(self.minheap) > self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]
    

    '''
    A heap can either be a min or max heap. In the min heap the min value
    will always be the first element and on the other hand the max element will
    be the first element in a max heap. In this case we are using a max heap that
    will only contain at most k elements, because k start from the largest and 
    goes does, we want to use a minheap to keep track of the kth largest elements.
    By using a loop to remove the smallest elements until k items are left, one will be left
    with the top k elements. The inital heapify function run in nlogn time, but the 
    add function runs in logn time as it only takes logn time to add to a heap
    the reason the heapify function takes nlogn as it takes log n to pop and may
    have to top for n-k*logn times. which is just nlogn
    '''
