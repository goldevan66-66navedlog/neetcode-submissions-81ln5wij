class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        
        groupNum = len(hand)//groupSize
        hand.sort() # sorts the hand in incresing order

        lst = [[] for i in range(len(hand)//groupSize)]
        prev = -1
        group = -1
        nextAvail = 0
        for i in range(len(hand)):
            if(prev != hand[i]):
                group = nextAvail
            else:
                group += 1

            if(group >= groupNum or (len(lst[group])>0 and hand[i]-lst[group][-1]!=1)):
                return False
            # while(len(lst[group])==groupSize):
            #     group += 1
            # if(group > groupNum):
            #     return False

            # if(len(lst[group])>0 and hand[i]-lst[group][-1]!=1):
            #     return False
            
            lst[group].append(hand[i])
            if(len(lst[group])==groupSize):
                nextAvail +=1
            prev = hand[i]
        
        
        return True

            
