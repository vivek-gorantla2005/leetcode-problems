class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, maxi):
            if not node:
                return
            
            if node.val >= maxi:
                self.ans += 1
            
            maxi = max(maxi, node.val)

            dfs(node.left, maxi)
            dfs(node.right, maxi)

        dfs(root, float('-inf'))
        return self.ans
