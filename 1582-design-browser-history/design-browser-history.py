class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        self.curr = node

    def visit(self, val):
        node = Node(val)
        
        self.curr.next = None

        node.prev = self.curr
        self.curr.next = node

        self.curr = node
        self.tail = node

    def back(self, steps):
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps):
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = DLL(homepage)

    def visit(self, url: str) -> None:
        self.history.visit(url)

    def back(self, steps: int) -> str:
        return self.history.back(steps)

    def forward(self, steps: int) -> str:
        return self.history.forward(steps)
