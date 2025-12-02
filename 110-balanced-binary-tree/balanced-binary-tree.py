class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag = 0
        def dfs(node):
            if not node:
                return 0
            
            right = dfs(node.right)
            left = dfs(node.left)
            if abs(left-right) > 1 : self.flag = 1
            return 1+max(left,right)
        dfs(root)
        return True if self.flag == 0 else False
        