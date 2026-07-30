class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0

        for i in range(len(cost)-1,-1,-1):
            temp = one
            one = min(cost[i]+one,cost[i]+two)
            two = temp
        
        return min(one,two)

        # one, two = len(cost)-1, len(cost)-2
        # res = 0
        # while(one >= 0 and two >= 0):
        #     print(f"One: {one} and two: {two}")
        #     if(cost[one]<cost[two]):
        #         res += cost[one]
        #         two = one-2
        #         one = one-1
        #         print(f"One: {one} and two: {two}")
        #     else:
        #         res += cost[two]
        #         one = two-1
        #         two = two-2
        #         print(f"One: {one} and two: {two}")
        # return res

