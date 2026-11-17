class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        counts = {}
        
        for n in nums:
            counts[n] = counts.get(n,0)+1
        
        for j in counts.keys():
            freq[counts[j]].append(j)
        
        res = []
        p = len(freq)-1
        
        while(True):
            for i in freq[p]:
                res.append(i)
                if(len(res) == k):
                    return res
            p -= 1
        
