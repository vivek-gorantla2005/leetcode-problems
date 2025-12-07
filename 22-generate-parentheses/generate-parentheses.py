class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(curr,open,close):
            if open == n and close == n:
                ans.append(curr)
                return
            if open < n:
                curr+="("
                dfs(curr,open+1,close)
                curr = curr[:-1]
            if close < open:
                curr+=")"
                dfs(curr,open,close+1)
                curr = curr[:-1]
        dfs("",0,0)
        return ans
            
        