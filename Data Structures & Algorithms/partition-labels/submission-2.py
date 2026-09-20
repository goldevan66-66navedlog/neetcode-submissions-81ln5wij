class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Neetcodes solution
        indexs = {}
        res = []
        for i,c in enumerate(s):
            indexs[c] = i
        
        size = 0
        end = 0
        for i in range(len(s)):
            end = max(end,indexs[s[i]])
            size += 1

            if(i == end):
                res.append(size)
                size = 0
        
        return res

        # My solution
        # counts = {}
        # for c in s:
        #     counts[c] = counts.get(c,0)+1
        
        # res = []
        # temp = ""
        # seen = set()
        # for i in range(len(s)):
        #     counts[s[i]] -= 1
        #     seen.add(s[i])
        #     if(counts[s[i]] == 0):
        #         seen.remove(s[i])

        #     temp = temp + s[i]

        #     if(not seen):
        #         res.append(len(temp))
        #         temp = ""
        
        # return res



        
