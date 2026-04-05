# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while(list1 and list2):
            if(list1.val < list2.val):
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        if(list1):
            node.next = list1
        else:
            node.next = list2
        
        return dummy.next

        # My way of solving, a bit vervose but got the job done
        # if(list1 and list2):
        #     if(list1.val > list2.val):
        #         tmp = list1
        #         list1 = list2
        #         list2 = tmp
        
        # curr1 = list1
        # curr2 = list2
        
        # while(curr1):
        #     if(curr1.next == None):
        #         curr1.next = curr2
        #         return list1
        #     elif(curr2 == None):
        #         return list1
        #     elif(curr2.val >= curr1.val and curr2.val <= curr1.next.val):
        #         nxt1 = curr1.next
        #         nxt2 = curr2.next
        #         curr1.next = curr2
        #         curr2.next = nxt1
        #         curr2 = nxt2 
        #         curr1 = curr1.next
        #         print(curr1)
        #     else:
        #         curr1 = curr1.next
        
        # return list1 if list1 else list2
        