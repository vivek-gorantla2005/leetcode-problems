class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        def reverse(temp):
            prev = None
            while temp:
                nextNode = temp.next
                temp.next = prev
                prev = temp
                temp = nextNode
            return prev
        
        def getKthNode(temp, k):
            k -= 1
            while temp and k > 0:
                temp = temp.next
                k -= 1
            return temp
        
        temp = head
        prevTail = None
        
        while temp:
            kth = getKthNode(temp, k)
            
            if not kth:
                if prevTail:
                    prevTail.next = temp
                break
            
            nextGroup = kth.next
            kth.next = None
            
            newHead = reverse(temp)
            
            if temp == head:
                head = newHead
            else:
                prevTail.next = newHead
            
            prevTail = temp
            temp = nextGroup
        
        return head