class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # tmp = [i for i in range(m+1)]

        l,r = 1,max(piles)
        res = float("inf")

        while(l<=r):
            m = l + (r-l)//2
            times = [math.ceil(p/m) for p in piles]
            totalt = sum(times)

            if(totalt <= h):
                r = m-1
                res = min(res,m)
            elif(totalt > h):
                l = m+1
        
        return res