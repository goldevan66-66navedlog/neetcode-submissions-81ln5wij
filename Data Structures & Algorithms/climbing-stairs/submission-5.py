class Solution:
    def climbStairs(self, n: int) -> int:
        # if(n==0):
        #     return 1
        # if(n < 0):
        #     return 0
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        res = {i:0 for i in range(n+1)}
        res[0] = 0
        res[1] = 1
        res[2] = 2

        if(n>=3):
            for k in range(3,n+1):
                for j in [1,2]:
                    if(k-j in res):
                        res[k]+=res[k-j]
        return res[n]