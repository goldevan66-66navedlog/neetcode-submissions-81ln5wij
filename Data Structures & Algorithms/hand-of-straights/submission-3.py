class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        
        groupNum = len(hand)//groupSize
        hand.sort() # sorts the hand in incresing order

        lst = [[] for i in range(len(hand)//groupSize)]
        prev = -1
        group = -1
        for i in range(len(hand)):
            if(prev != hand[i]):
                group = 0
            else:
                group += 1
            if(group not in range(groupNum)):
                return False
            while(len(lst[group])==groupSize):
                group += 1
                if(group > groupNum):
                    return False

            if(len(lst[group])>0 and hand[i]-lst[group][-1]!=1):
                return False
            lst[group].append(hand[i])
            prev = hand[i]
        
        
        return True

            
