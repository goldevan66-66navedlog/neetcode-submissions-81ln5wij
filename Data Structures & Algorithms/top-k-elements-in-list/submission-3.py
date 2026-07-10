class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Is the input sorted?
        freq = [[] for i in range(len(nums)+1)]

        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1

        for j in d.keys():
            freq[d[j]].append(j)
        
        res = []
        for i in range(len(freq)):
            if(len(res)<k):
                res += freq[-i]
        
        return res

