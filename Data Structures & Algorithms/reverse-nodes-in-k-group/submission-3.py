# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        gP = dummy

        while(True):
            kth = self.getKth(gP,k)
            if not kth:
                break
            gN = kth.next

            prev, curr = kth.next, gP.next

            while(curr != gN):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = gP.next
            gP.next = kth
            gP = temp
        return dummy.next
        
    def getKth(self,node,k):
        while(node and k>0):
            node = node.next
            k-=1
        return node
    #     l = 0 # this is the length
    #     curr = head
    #     while(curr):
    #         l += 1
    #         curr = curr.next
        
    #     if(k > l):
    #         return head

    #     count = 0
    #     reverse = l//k
    #     curr = head
    #     tmp = None
    #     prev = None

    #     while(count < reverse):
    #         start, stop = self.reverseList(curr,k)
    #         if(count == 0):
    #                 tmp = start
    #         if(prev):
    #             prev.next = start
    #         if(stop):
    #             curr = stop.next
    #         prev = stop
    #         count += 1
    #     return tmp



    # def reverseList(self, h, k):
    #     prev = None
    #     count = 0
    #     curr = h
    #     while(curr and count<k):
    #         nxt = curr.next
    #         curr.next = prev
    #         prev  = curr
    #         curr = nxt
    #         count += 1
    #     if(h):
    #         h.next = curr
        
    #     return [prev,h]
        