class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        chars = {c:[] for w in words for c in w}
        visited = {}
        res = []

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minlen = min(len(w1), len(w2))
            if(len(w1)>len(w2) and w1[:minlen]==w2[:minlen]):
                return ""
            for i in range(minlen):
                if(w1[i] != w2[i]):
                    chars[w1[i]].append(w2[i])
                    break
        
        def dfs(c):
            if(c in visited):
                return visited[c]
            visited[c] = True

            for nei in chars[c]:
                if(dfs(nei)):
                    return True
            visited[c] = False
            res.append(c)

        for c in chars.keys():
            if(dfs(c)):
                return ""
        
        return "".join(res[::-1])


        