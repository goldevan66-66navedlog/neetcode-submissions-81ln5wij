# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sz = 0
        # curr = head
        # while(curr):
        #     sz += 1
        #     curr = curr.next

        # node = sz - n
        # prev = None
        # curr = head
        # index = 0
        # while(index != node):
        #     index += 1
        #     prev = curr
        #     curr = curr.next
    
        # if(prev):
        #     prev.next = curr.next
        # else:
        #     head = head.next
        
        # return head
        
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while(right):
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return dummy.next
        

        

