class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = []
        def dfs(node):
            if not node:
                return
            
            if node:
                ans.append(node)


            if node.child:
                dfs(node.child)

            dfs(node.next)
        
        dfs(head)

        for i in range(len(ans)):
            if i > 0:
                ans[i].prev = ans[i-1]
                ans[i-1].next = ans[i]
            ans[i].child = None 
        
        return ans[0] if ans else None

        
        
            
        