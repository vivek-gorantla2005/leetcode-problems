class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smalldummy = ListNode(0)
        largedummy = ListNode(0)
        l1 = smalldummy
        l2 = largedummy
        temp = head
        while temp:
            if temp.val < x:
                l1.next = temp
                l1 = l1.next
            else:
                l2.next = temp
                l2 = l2.next
            temp = temp.next

        l2.next = None
        l1.next = largedummy.next

        return smalldummy.next

        