class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0

        # while(n):
        #     bits += n % 2
        #     n = n >> 1

        # return bits

        while(n):
            n &= (n-1)
            bits += 1
        return bits

        # n = bin(n)[2:].replace("0",'')
        # return len(n)
        