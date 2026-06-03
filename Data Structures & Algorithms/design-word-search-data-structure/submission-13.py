class TrieNode():
    def __init__(self):
        self.children = {}
        self.exist = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        lst = self.trie
        for w in word:
            if(w not in lst.children):
                lst.children[w] = TrieNode()
            lst = lst.children[w]
        lst.exist = True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if(c == "."):
                    for child in curr.children.values():
                        if(dfs(i+1,child)):
                            return True
                    return False
                else:
                    if(c not in curr.children):
                        return False
                    curr = curr.children[c]
            return curr.exist
        return dfs(0,self.trie)
