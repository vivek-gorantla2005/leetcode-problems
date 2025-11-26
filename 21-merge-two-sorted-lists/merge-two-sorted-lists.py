class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        
        dummy = ListNode()   
        temp = dummy          
        
        while t1 and t2:
            if t1.val <= t2.val:
                temp.next = t1   
                t1 = t1.next     
            else:
                temp.next = t2
                t2 = t2.next

            temp = temp.next    

        temp.next = t1 if t1 else t2

        return dummy.next
