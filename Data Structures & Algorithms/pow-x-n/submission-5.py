class Solution:
    def myPow(self, x: float, n: int) -> float:
        start = float(1)
        if(n == 0 or x == 1):
            return 1

        if(x == -1):
            return 1 if n%2==0 else -1

        for i in range(abs(n)):
            if(n > 0):
                start  = start * x
                if(start >= 10000):
                    return 10000
            else:
                start  = start * x
                if(float(1/start) <= 0.00001):
                    return 0
            

        return start if n>0 else float(1/start)
        