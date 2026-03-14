class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        chars = ["a", "b", "c"]

        def dfs(curr):
            if len(curr) == n:
                ans.append(curr)
                return
            
            for c in chars:
                if not curr or curr[-1] != c:
                    dfs(curr + c)

        dfs("")

        if k > len(ans):
            return ""
        return ans[k-1]
