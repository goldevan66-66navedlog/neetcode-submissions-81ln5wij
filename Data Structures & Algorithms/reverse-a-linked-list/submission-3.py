# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        curr = head
        while(curr):
            temp = curr.next
            curr.next = last
            last = curr
            # if(temp!=None):
            curr = temp
            # else:
            #     return head
        return last


        