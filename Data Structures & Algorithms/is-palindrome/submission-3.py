class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = "".join([c for c in s if(c in valid) ])
        left = 0
        right = len(s)-1

        while(right >= left):
            if(s[left]!= s[right]):
                return False
            left += 1
            right -= 1
        
        return True
