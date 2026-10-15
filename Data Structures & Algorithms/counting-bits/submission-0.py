class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]

        if(n == 0):
            return [0]

        for i in range(1,n+1):
            bits = 0
            temp = i
            while(temp):
                bits += temp%2
                temp = temp >> 1
            res.append(bits)
        
        return res
        