class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = {}
        for c in s:
            counts[c] = counts.get(c,0)+1
        
        # seen = set()
        # seen.add(s[0])
        # counts[s[0]] -= 1

        # res = []

        # sub = s[0]
        # start = 1
        
        # while(start<len(s)):
        #     while(seen and start < len(s)):
        #         counts[s[start]] -= 1

        #         if(counts[s[start]]==0):
        #             seen.remove(s[start])
        #         else:
        #             seen.add(s[start])
                
        #         sub = sub + s[start] 
        #         start += 1

        #     res.append(len(sub))
        
        #     if(start < len(s)):
        #         sub = s[start]
        #         seen.add(s[start])
        #         counts[s[start]] -= 1
        #         start += 1
        
        # # res.append(len(sub))
        # return res
        res = []
        temp = ""
        seen = set()
        for i in range(len(s)):
            counts[s[i]] -= 1
            seen.add(s[i])
            if(counts[s[i]] == 0):
                seen.remove(s[i])

            temp = temp + s[i]

            if(not seen):
                res.append(len(temp))
                temp = ""
        
        return res



        
