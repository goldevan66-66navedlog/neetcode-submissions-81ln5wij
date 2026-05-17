class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while(maxHeap or q):
            time += 1
            if(maxHeap):
                cnt = 1 + heapq.heappop(maxHeap)
                if(cnt):
                    q.append([cnt,time+n])
            if(q and q[0][1]==time):
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
                

