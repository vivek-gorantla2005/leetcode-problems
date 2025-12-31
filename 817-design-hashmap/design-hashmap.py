class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.size = 10**4
        self.map = [ListNode(-1, -1) for _ in range(self.size)]  # dummy heads

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.size
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        curr = self.map[idx]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
