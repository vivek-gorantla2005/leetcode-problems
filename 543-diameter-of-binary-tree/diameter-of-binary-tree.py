class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxi = 0
        def dfs(node):
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxi = max(self.maxi,left+right)
            return 1+max(left,right)
        dfs(root)
        return self.maxi
        