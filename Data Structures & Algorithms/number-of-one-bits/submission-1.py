class Solution:
    def hammingWeight(self, n: int) -> int:
        # bits = 0

        # while(n>=2):
        #     bits += 1
        #     if(math.log(n))
        #     n = n//2

        # return bits

        n = bin(n)[2:].replace("0",'')
        return len(n)
        