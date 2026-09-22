class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin, leftmax = 0,0

        for c in s:
            if(c == "("):
                leftmin, leftmax = leftmin+1, leftmax+1
            elif(c == ")"):
                leftmin, leftmax = leftmin-1, leftmax-1
            else:
                leftmin, leftmax = leftmin-1, leftmax+1
            if(leftmax < 0):
                return False
            if(leftmin < 0):
                leftmin = 0
        
        return leftmin == 0
        # counts = {}

        # for c in s:
        #     counts[c] = counts.get(c,0)+1
       
        # for c in s:
        #     if(c == "("):
        #         if(counts.get(")",0) > 0):
        #             counts[c] -= 1
        #             counts[")"] -= 1
        #         elif(counts.get("*",0)>0):
        #             counts[c] -= 1
        #             counts["*"] -= 1
        #     if(c == "*"):
        #         if(counts.get(")",0) > 0):
        #             counts[c] -= 1
        #             counts[")"] -= 1
        
        # return False if (counts["("]>0 or counts[")"]>0) else True
        

