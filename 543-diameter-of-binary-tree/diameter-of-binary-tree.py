class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def dfs(node):
            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)
            self.maxi = max(self.maxi,left+right)
            return 1+max(right,left)
        dfs(root)
        return self.maxi
        