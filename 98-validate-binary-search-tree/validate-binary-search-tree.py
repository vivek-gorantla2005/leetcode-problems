class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.flag = True

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            if self.prev != None and self.prev >= node.val:
                self.flag = False
                return

            self.prev = node.val

            dfs(node.right)
        
        dfs(root)
        
        return self.flag
        