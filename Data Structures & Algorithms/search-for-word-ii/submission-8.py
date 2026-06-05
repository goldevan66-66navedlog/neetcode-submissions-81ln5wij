class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
    def addword(self,w):
        root = self
        for c in w:
            if(c not in root.children):
                root.children[c] = TrieNode()
            root = root.children[c]
        root.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for w in words:
            trie.addword(w)
        
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(i,j,node, word):
            if(i < 0 or i >= ROWS or j < 0 or j >= COLS or (i,j) in visited or board[i][j] not in node.children):
                return 

            visited.add((i,j))
            node = node.children[board[i][j]]
            word += board[i][j]
            if(node.word):
                res.add(word)
            
            dfs(i+1,j,node,word)
            dfs(i-1,j,node,word)
            dfs(i,j+1,node,word)
            dfs(i,j-1,node,word)
            visited.remove((i,j))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,trie,"")
        return list(res)
        # ROWS, COLS = len(board), len(board[0])
        # res = []
        # woords = set(words)
        # def dfs(i,j,word,target,k):
        #     if(i >= ROWS or i < 0 or j >= COLS or j < 0 or board[i][j]=="*" or len(word)==len(target) or board[i][j]!=target[k]):
        #         copy = "".join(word) 
        #         if(copy in woords):
        #             woords.remove(copy)
        #             res.append(copy)
        #         return
        #     c = board[i][j]    
        #     word.append(c)
        #     board[i][j] = "*"
        #     dfs(i-1,j,word,target,k+1)
        #     dfs(i+1,j,word,target,k+1)
        #     dfs(i,j-1,word, target, k+1)
        #     dfs(i,j+1,word, target, k+1)
        #     board[i][j] = c
        #     word.pop()
        #     return
        
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         for w in words:
        #             dfs(i,j,[],w,0)
        # return res
