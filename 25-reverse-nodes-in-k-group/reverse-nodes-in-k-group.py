class Solution:
    def getknode(self, curr, k):
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, curr, k):
        prev = None
        temp = curr
        while k > 0:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
            k -= 1
        return prev, curr  # new head, new tail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGrp = dummy

        while True:
            temp = prevGrp.next
            kNode = self.getknode(temp, k)
            if kNode is None:
                break

            nxt = kNode.next
            newHead, newTail = self.reverse(temp, k)

            prevGrp.next = newHead
            newTail.next = nxt

            prevGrp = newTail

        return dummy.next
