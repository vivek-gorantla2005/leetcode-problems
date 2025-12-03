class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while len(q) > 0:
            curr = []
            for i in range(len(q)):
                f = q.popleft()
                curr.append(f.val)

                if f.left:
                    q.append(f.left)
                if f.right:
                    q.append(f.right)

            ans.append(curr)

        return ans
