class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if(n == 0):
            return 1
        if(x == -1):
            return -1 if n%2 else 1
        
        def helper(x,n):
            if(n == 0):
                return 1
            if(x == 0):
                return 0
            
            res = helper(x*x,n//2)

            return res*x if n%2 else res
            
        
        r = helper(x,abs(n))
        return 1/r if n<0 else r
        # start = float(1)
        # if(n == 0 or x == 1):
        #     return 1

        # if(x == -1):
        #     return 1 if n%2==0 else -1

        # for i in range(abs(n)):
        #     if(n > 0):
        #         start  = start * x
        #         if(start >= 10000):
        #             return 10000
        #     else:
        #         start  = start * x
        #         if(float(1/start) <= 0.00001):
        #             return 0
            

        # return start if n>0 else float(1/start)
        