class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = 0
        size = 0
        s = 0
        res = 0

        while(r < len(arr)):
            s += arr[r]
            size += 1

            if(size == k):
                if(s/k >= threshold):
                    res += 1
                size -= 1
                s -= arr[l]
                l += 1
            r += 1
        
        return res

