class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = {}
        ana2 = {}

        if(len(s) != len(t)):
            return False
        
        for i in range(len(s)):
            ana1[s[i]] = ana1.get(s[i],0)+1
            ana2[t[i]] = ana2.get(t[i],0)+1
        
        return ana1 == ana2