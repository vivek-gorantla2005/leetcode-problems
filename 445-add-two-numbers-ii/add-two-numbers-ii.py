class Solution:
    def addTwoNumbers(self, l1, l2):
        st1 = []
        st2 = []
        
        while l1:
            st1.append(l1.val)
            l1 = l1.next
        
        while l2:
            st2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None 
        
        while st1 or st2 or carry:
            val1 = st1.pop() if st1 else 0
            val2 = st2.pop() if st2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            
            node = ListNode(total % 10)
            node.next = head
            head = node
        
        return head