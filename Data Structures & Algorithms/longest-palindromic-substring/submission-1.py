class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        for i in range(len(s)):
            curr = s[i]
            for j in range(i+1,len(s)):
                curr = curr + s[j]
                if(self.isPalin(curr)):
                    if(len(curr)> len(res)):
                        res = curr
        return res

        

    def isPalin(self,s):
        return s == s[::-1]
        