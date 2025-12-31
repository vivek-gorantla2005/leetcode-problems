class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.size = 10**4
        self.set = [ListNode(0) for _ in range(self.size)] 

    def add(self, key: int) -> None:
        curr = self.set[key % self.size]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.set[key % self.size]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.set[key % self.size]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False
