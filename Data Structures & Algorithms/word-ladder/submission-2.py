# class Node:
#     def __init__(self, word, count):
#         self.word = word
#         self.count = count

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if(endWord not in wordList):
            return 0
        nei = collections.defaultdict(list)
        wordList.append(beginWord)

        for w in wordList: # gets the words that match the pattern to create an adjaceny list nei
            for j in range(len(w)):
                pattern  = w[:j] + "*" + w[j+1:]
                nei[pattern].append(w)

        q = deque()
        res= 1
        visit = set(beginWord)
        q.append(beginWord)
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if(word == endWord): #exits the bfs
                    return res
                for j in range(len(word)):
                    pattern  = word[:j] + "*" + word[j+1:] #gets the pattern to see the words neighbors and bc in visited won't visit itself
                    for neis in nei[pattern]:
                        if(neis not in visit): 
                            visit.add(neis)
                            q.append(neis)
            res += 1 # this is really the level of the graph and once a word is found while traversing add one to the result
        return 0 #if the bfs exits then the word does not exists an therefore return 0

        # def charCount(w):
        #     count = {}
        #     for c in w:
        #         count[c] = 1 + count.get(c,0)
        #     return count
        
        # counts = []
        # words = []
        # counts.append(Node(beginWord,charCount(beginWord)))
        # words.append(beginWord)
        # counts.append(Node(endWord,charCount(endWord)))
        # words.append(endWord)
        # for w in wordList:
        #     counts.append(Node(w,charCount(w)))
        #     words.append(w)
        
        # edges = []

        # for i in range(len(counts)):
        #     for j in range(i+1,len(counts)):
        #         c1 = counts[i].count
        #         c2  =counts[j].count
        #         dif = 0
        #         for k in c1.keys():
        #             if(c2.get(k,0) == 0):
        #                 dif += 1
                
        #         if(dif == 1):
        #             edges.append([counts[i].word, counts[j].word])
     
        # adj = {w:[] for w in words}

        # for e1, e2 in edges:
        #     adj[e1].append(e2)
        #     adj[e2].append(e1)
        
        # visited = set()
        # def dfs(w,prev):
        #     if(w == endWord):
        #         return 0
        #     if(w in visited):
        #         return float("inf")
        #     for wrd in adj[w]:
        #         visited.add(wrd)
        #         mini = float("inf")
        #         if(wrd == prev):
        #             continue
        #         mini = min(dfs(wrd,w)+1,mini)
        #         visited.remove(wrd)
        #     return mini
        # res = dfs(beginWord,"")
        # print(res)
        # return res