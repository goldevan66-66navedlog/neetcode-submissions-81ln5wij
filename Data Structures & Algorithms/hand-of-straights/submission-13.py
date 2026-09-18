class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize):
            return False
        
        count = {}
        for n in hand:
            count[n] = count.get(n,0)+1
        
        nums = list(count.keys())
        heapq.heapify(nums)

        while(nums):
            start = nums[0]

            for i in range(start,start+groupSize):
                if(i not in count):
                    return False
                count[i] -=1
                if(count[i]==0):
                    if(i != nums[0]):
                        return False
                    heapq.heappop(nums)
        return True

        # if(len(hand)%groupSize != 0):
        #     return False
        
        # groupNum = len(hand)//groupSize
        # hand.sort() # sorts the hand in incresing order

        # lst = [[] for i in range(groupNum)]
        # prev = -1
        # group = -1
        # nextAvail = 0
        # for i in range(len(hand)):
        #     if(prev != hand[i]):
        #         group = nextAvail
        #     else:
        #         group += 1

        #     if(group >= groupNum or (len(lst[group])>0 and hand[i]-lst[group][-1]!=1)):
        #         return False

        #     lst[group].append(hand[i])

        #     if(len(lst[group])==groupSize):
        #         nextAvail +=1

        #     prev = hand[i]
        
        
        # return True

            
