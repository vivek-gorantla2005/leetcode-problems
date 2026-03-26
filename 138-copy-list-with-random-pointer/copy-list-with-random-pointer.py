class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {None:None}
        curr = head
        while curr:
            copyMap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copynode = copyMap[curr]
            copynode.next = copyMap[curr.next]
            copynode.random = copyMap[curr.random]
            curr = curr.next
        
        return copyMap[head]
        