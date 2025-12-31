class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([root])

        while q:
            level = []
            l = len(q)
            for _ in range(l):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)
                
                if n.right:
                    q.append(n.right)
            ans.append(level)
        return ans


        
