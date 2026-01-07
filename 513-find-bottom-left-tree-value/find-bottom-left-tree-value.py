class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        ans = []
        while len(q) > 0:
            curr = []
            for _ in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(curr)
        return ans[-1][0]
