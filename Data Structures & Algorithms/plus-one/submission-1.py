class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0

        for i in range(len(digits)-1,-1,-1):
            number += (10**(len(digits)-1-i))*digits[i]
        
        number += 1

        return [int(c) for c in str(number)]

        