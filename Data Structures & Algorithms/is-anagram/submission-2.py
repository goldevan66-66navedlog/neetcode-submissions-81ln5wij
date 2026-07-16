class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i],0)+1
            countT[t[i]] = countT.get(t[i],0)+1

        for k in countS.keys():
            if(k not in countT):
                return False
            if(countS[k] != countT[k]):
                return False

        return True