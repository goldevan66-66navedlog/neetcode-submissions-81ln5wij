class Solution:
    def countBits(self, n: int) -> List[int]:

        res = [0]*(n+1)
        offset = 1

        for i in range(1,n+1):
            if(offset*2 == i):
                offset = i
            res[i] = 1 + res[i-offset]
        
        return res

        # for i in range(1,n+1):
        #     bits = 0
        #     temp = i
        #     while(temp):
        #         bits += temp%2
        #         temp = temp >> 1
        #     res.append(bits)
        
        return res
        