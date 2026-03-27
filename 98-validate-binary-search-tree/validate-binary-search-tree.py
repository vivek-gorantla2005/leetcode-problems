class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        for i in range(len(ans)):
            if i > 0 and ans[i-1] >= ans[i]:
                return False
        
        return True


        