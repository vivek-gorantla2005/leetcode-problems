class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def dfs(node):
            if not node :
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.arr[k-1]
        