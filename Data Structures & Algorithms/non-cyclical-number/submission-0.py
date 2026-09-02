class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}

        while(n != 1):
            if(n in seen):
                return False
            seen[n] = 1
            temp = 0
            for c in str(n):
                temp += int(c)**2
            
            n = temp
        
        return True
        