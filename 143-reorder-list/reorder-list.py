# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # 1. Find middle
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. Reverse second half
        second = slow.next
        prev = slow.next = None  
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # 3. Merge both halves: head (first half) & prev (second half reversed)
        first = head
        second = prev
        
        while second:
            # save next pointers
            tmp1 = first.next
            tmp2 = second.next
            
            # weave nodes: first → second
            first.next = second
            second.next = tmp1
            
            # move forward
            first = tmp1
            second = tmp2
        
        return
