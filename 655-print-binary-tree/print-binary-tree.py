class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        h = height(root)
        
        rows = h
        cols = (2 ** h) - 1
        ans = [[""] * cols for _ in range(rows)]

        def dfs(node, r, c):
            if not node:
                return

            ans[r][c] = str(node.val)

            offset = 2 ** (h - r - 2)
            if node.left:
                dfs(node.left, r + 1, c - offset)
            if node.right:
                dfs(node.right, r + 1, c + offset)

        dfs(root, 0, (cols - 1) // 2)
        return ans
