class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(node,curr,target):
            if not node:
                return
            
            curr.append(node.val)
            target-=node.val
        
            if target == 0 and (not node.left and not node.right):
                ans.append(curr[:])
            
            dfs(node.left,curr,target)
            dfs(node.right,curr,target)
            curr.pop()

        dfs(root,[],targetSum)
        return ans
        