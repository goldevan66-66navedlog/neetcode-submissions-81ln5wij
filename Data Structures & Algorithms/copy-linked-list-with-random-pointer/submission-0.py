"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {None: None}

        curr = head

        while(curr):
            tmp = Node(curr.val)
            dic[curr] = tmp
            curr = curr.next
        
        curr = head

        while(curr):
            nod = dic[curr]
            nod.next = dic[curr.next]
            nod.random = dic[curr.random]
            curr = curr.next
        
        return dic[head]


