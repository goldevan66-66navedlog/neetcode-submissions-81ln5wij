class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ints = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

        sumi= 0 

        # for i in range(len(num1)-1,-1,-1):
        #     for j in range(len(num2)-1,-1,-1):
        #         sumi += ints[num1[i]]*10**(len(num1)-1-i)*ints[num2[j]]*10**(len(num2)-1-j)

        int1 = 0
        for i in range(len(num1)-1,-1,-1):
            int1 += ints[num1[i]]*10**(len(num1)-1-i)
        
        int2 = 0
        for j in range(len(num2)-1,-1,-1):
            int2 += ints[num2[j]]*10**(len(num2)-1-j)
        
        
        return str(int1*int2)