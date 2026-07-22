class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = left

        res = 0
        temp = set()

        while(right < len(s)):
            if(s[right] not in temp):
                temp.add(s[right])
            else:
                res = max(res,len(temp))
                while(s[right] in temp):
                    temp.remove(s[left])
                    left += 1
                temp.add(s[right])
            right += 1

        res = max(res,len(temp))
        return res

