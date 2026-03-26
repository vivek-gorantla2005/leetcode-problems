# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        h2 = slow.next
        slow.next = None

        #reverse second half
        prev = None
        temp2 = h2
        while temp2:
            nxtnode = temp2.next
            temp2.next = prev
            prev = temp2
            temp2 = nxtnode

        t1 = head
        t2 = prev
        while t2:
            first = t1.next
            second = t2.next
            t1.next = t2
            t2.next = first

            t1 = first
            t2 = second
        
        return 
            



        