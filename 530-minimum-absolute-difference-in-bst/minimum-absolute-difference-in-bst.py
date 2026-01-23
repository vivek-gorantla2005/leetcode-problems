class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder = []
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            self.inorder.append(node.val)
            right = dfs(node.right)
        dfs(root)
        
        mini = float('inf')
        for i in range(1,len(self.inorder)):
            mini = min(mini,abs(self.inorder[i]-self.inorder[i-1]))
        
        return mini

        