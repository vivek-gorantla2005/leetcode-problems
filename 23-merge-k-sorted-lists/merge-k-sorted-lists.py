class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None
        
        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            
            return dummy.next
        
        while len(lists) > 1:
            curr = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                merged = mergeTwoLists(l1, l2)
                curr.append(merged)
            
            lists = curr
        
        return lists[0]