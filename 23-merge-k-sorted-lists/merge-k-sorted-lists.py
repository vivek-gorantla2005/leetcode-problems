class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2lists(head1,head2):
            t1 = head1
            t2 = head2
            dummy = ListNode(0)
            temp = dummy
            while t1 and t2:
                if t1.val <= t2.val:
                    temp.next = t1
                    t1 = t1.next
                else:
                    temp.next = t2
                    t2 = t2.next
                temp = temp.next
            
            if t1:
                temp.next = t1
            
            if t2:
                temp.next = t2
            
            return dummy.next
        
        if not lists:
            return None
        
        while len(lists) > 1:
            curr = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                curr.append(merge2lists(l1,l2))
            lists = curr

        return lists[0]
            
            
        