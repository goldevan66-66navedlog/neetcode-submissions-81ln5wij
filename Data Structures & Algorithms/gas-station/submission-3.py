class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # cumul = 0
        # start = 0
        # i = 0

        # for g,c in zip(gas,cost):
        #     if(g+cumul<c):
        #         start = i+1
        #     cumul += g-c
        #     i += 1
   
        # return start if cumul>=0 else -1

        total = 0
        start = 0

        if(sum(gas)< sum(cost)):
            return -1
        
        for i in range(len(gas)):
            if(total+gas[i]-cost[i]<0):
                start = i+1
                total = 0
            else:
                total += gas[i]-cost[i]
        return start if total >=0 else -1
