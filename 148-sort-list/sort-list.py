class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        def merge2lists(head1, head2):
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

        def findMid(temp):
            slow = temp
            fast = temp
            prev = None
            
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None   
            
            return slow
        
        def divide(temp):
            if not temp or not temp.next:
                return temp
            
            left = temp
            right = findMid(temp)
            
            left = divide(left)
            right = divide(right)
            
            return merge2lists(left, right)
        
        return divide(head)