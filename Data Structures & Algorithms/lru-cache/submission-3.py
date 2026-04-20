class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key, pointer
        self.left, self.right = Node(0,0), Node(0,0) #this will be a doubly linked list
        self.left.next = self.right
        self.right.prev = self.left
    
    #delete a node from the linkedlist
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # add a node to the right of the linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        

    def get(self, key: int) -> int:
        if(key in self.cache):
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if(key in self.cache):
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if(len(self.cache) > self.cap):
            lru = self.left.next
            del self.cache[lru.key]
            self.delete(lru)


        
