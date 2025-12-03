class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        while len(q) > 0 :
            curr = []
            for i in range(len(q)):
                currele = q[0]
                curr.append(currele.val)
                q.popleft()
                if currele.left:
                    q.append(currele.left)
                if currele.right:
                    q.append(currele.right)
            ans.append(curr)
        
        final = []
        for i in ans:
            final.append(i[-1])
        return final
        