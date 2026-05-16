class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t,0)+1
        
        counts = [counts[k]*-1 for k in counts.keys()]

        heapq.heapify(counts)
        time = 0
        q = deque()
        while(counts or q):
            time += 1
            if(not counts):
                time = q[0][1]
            else:
                tmp = heapq.heappop(counts)
                print(tmp)
                cnt = 1 + tmp
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][1] == time:
                heapq.heappush(counts,q.popleft()[0])
        return time
                

