class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks) #getting the counts of task types
        maxHeap = [-cnt for cnt in count.values()] #negating to create a maxheap
        heapq.heapify(maxHeap) #O(n) time to make a maxheap
        time = 0 #keeps track of the processing time
        q = deque() #stores values [count, next_availible_time]

        while(maxHeap or q): # only runs if there are task left to run
            time += 1 #if this code is excuting then time is passing by
            if(maxHeap): #procces the most frequent task first
                cnt = 1 + heapq.heappop(maxHeap) # add one to the count as counts are negative for max heap
                if(cnt): # if there exist a count then add to queue as will have some idle time
                    q.append([cnt,time+n])
            else: #if only the queue exist then fast-forward in time to reach the next aviable time if the heap is empty
                time = q[0][1]
            if(q and q[0][1]==time): #adds back to the heap when next_avaiable time is equal to the global time
                heapq.heappush(maxHeap, q.popleft()[0])
        return time


        # counts = {}
        # for t in tasks:
        #     counts[t] = counts.get(t,0)+1
        
        # counts = [counts[k]*-1 for k in counts.keys()]

        # heapq.heapify(counts)
        # time = 0
        # q = deque()
        # while(counts or q):
        #     time += 1
        #     if(not counts):
        #         time = q[0][1]
        #     else:
        #         tmp = heapq.heappop(counts)
        #         print(tmp)
        #         cnt = 1 + tmp
        #         if cnt:
        #             q.append([cnt, time+n])
        #     if q and q[0][1] == time:
        #         heapq.heappush(counts,q.popleft()[0])
        # return time
                

