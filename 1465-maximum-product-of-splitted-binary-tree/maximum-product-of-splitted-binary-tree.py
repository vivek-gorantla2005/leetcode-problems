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
        ans = 0
        maxi = float('-inf')
        for i in range(len(arr)-1):
            num2 = tot - arr[i]
            maxi = max(maxi,arr[i] * num2)
        return maxi%MOD



        