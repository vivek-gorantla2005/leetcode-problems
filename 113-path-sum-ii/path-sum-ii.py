class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        self.path = []
        def dfs(node,currSum):
            if not node:
                return 
            
            self.path.append(node.val)
            currSum+=node.val

            if not node.left and not node.right and currSum == targetSum:
                self.ans.append(self.path[:])
                self.path.pop()
                return
            
            left = dfs(node.left,currSum)
            right = dfs(node.right,currSum)
            self.path.pop()

        dfs(root,0)
        return self.ans
                
        