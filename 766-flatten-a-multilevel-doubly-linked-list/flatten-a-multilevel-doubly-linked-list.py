class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0) 
        self.temp = dummy

        def dfs(node):
            if not node:
                return
            
            newNode = Node(node.val)
            self.temp.next = newNode
            newNode.prev = self.temp
            self.temp = newNode

            if node.child:
                dfs(node.child)

            dfs(node.next)
        
        dfs(head)

        res = dummy.next
        if res:
            res.prev = None  
        
        return res