class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prefix = 0
        mp = {}
        node = dummy

        # First pass: map prefix sum to LAST node
        while node:
            prefix += node.val
            mp[prefix] = node
            node = node.next

        # Second pass: skip zero-sum ranges
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = mp[prefix].next
            node = node.next

        return dummy.next
