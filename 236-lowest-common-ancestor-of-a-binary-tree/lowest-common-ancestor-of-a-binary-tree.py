class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node or node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                return right
            
            if not right:
                return left

            if left and right:
                return node
            
        return dfs(root)