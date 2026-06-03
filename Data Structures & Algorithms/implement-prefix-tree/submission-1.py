class PrefixTree:

    def __init__(self):
        self.trie = {}
        

    def insert(self, word: str) -> None:
        lst = self.trie
        for w in word:
            if(w not in lst):
                lst[w] = {}
            lst = lst[w]
        lst["exist"] = True

    def search(self, word: str) -> bool:
        lst = self.trie
        for w in word:
            if(w in lst):
                lst = lst[w]
                continue
            return False
        return True if "exist" in lst else False

    def startsWith(self, prefix: str) -> bool:
        lst = self.trie
        for w in prefix:
            if(w in lst):
                lst = lst[w]
                continue
            return False
        return True
        