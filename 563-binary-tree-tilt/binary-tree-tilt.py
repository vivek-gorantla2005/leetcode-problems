class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tot  = 0
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            self.tot += abs(left-right)
            return left+right+node.val
        dfs(root)
        return self.tot
        
        return dfs(root)
        