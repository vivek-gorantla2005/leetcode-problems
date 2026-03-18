class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        arr = []
        MOD = 10**9+7
        def sumTree(root):
            if not root:
                return 0
            left = sumTree(root.left)
            right = sumTree(root.right)
            arr.append(root.val + left + right)
            return root.val + left + right
        
        tot = sumTree(root)
        maxi = float('-inf')
        for i in range(len(arr)-1):
            maxi = max(maxi,arr[i] * (tot - arr[i]))
        return maxi%MOD



        