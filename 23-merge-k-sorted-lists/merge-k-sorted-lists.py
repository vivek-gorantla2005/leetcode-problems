import heapq

class Solution:
    def mergeTwoLists(self,head1,head2):
        dummy = ListNode(0)
        t1 = head1
        t2 = head2
        curr = dummy
        while t1 and t2:
            if t1.val <= t2.val:
                curr.next = t1
                t1 = t1.next
            else:
                curr.next = t2
                t2 = t2.next
            curr = curr.next
        if t1:
            curr.next = t1
        if t2:
            curr.next = t2

        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            curr = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                curr.append(self.mergeTwoLists(l1,l2))
            lists = curr
        
        return lists[0] if lists else None
