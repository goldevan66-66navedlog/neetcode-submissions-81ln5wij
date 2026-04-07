# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()

        # while(head):
        #     if(head in visited):
        #         return True
        #     visited.add(head)
        #     head = head.next
        
        # return False
        if(not head or not head.next):
            return False

        slow = head
        fast = head.next

        while(fast):
            if(fast == slow):
                return True
            elif(not fast.next):
                return False
            slow = slow.next
            fast = fast.next.next
        
        return False