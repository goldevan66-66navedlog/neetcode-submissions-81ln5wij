# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy  = ListNode(0,ListNode())
        curr = dummy.next

        carry = 0
        while(l1 or l2 or carry!=0):
            num1 = 0
            num2 = 0
            if(l1):
                num1 = l1.val
                l1 = l1.next
            if(l2):
                num2 = l2.val
                l2 = l2.next
            suum = num1 + num2 + carry
            curr.val = suum%10
            carry = suum//10
            if(l1 or l2 or carry!=0):
                curr.next = ListNode()
                curr = curr.next
        
        return dummy.next
        