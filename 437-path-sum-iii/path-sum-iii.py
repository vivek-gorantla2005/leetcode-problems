class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0

        def dfs(node, currSum):
            if not node:
                return
            
            currSum += node.val
            if currSum == targetSum:
                self.ans += 1
            
            dfs(node.left, currSum)
            dfs(node.right, currSum)

        def helper(node):
            if not node:
                return
            
            dfs(node, 0)        
            helper(node.left)    
            helper(node.right)   

        helper(root)
        return self.ans
