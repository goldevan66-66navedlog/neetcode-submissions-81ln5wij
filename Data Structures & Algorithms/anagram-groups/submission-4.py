class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def getCharCount(st):
            counts = [0]*26
            for c in st:
                index = ord(c) - ord('a')
                counts[index] += 1
            return counts

        groups = {}

        for s in strs:
            key = tuple(getCharCount(s))
            groups[key] = groups.get(key,[]) + [s]


        return list(groups.values())