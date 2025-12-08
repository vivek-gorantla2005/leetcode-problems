class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def isValid(s):
            return len(s) == len(set(s))

        def dfs(idx, curr):
            if idx == len(arr):
                return len(curr) if isValid(curr) else 0
        
            notPick = dfs(idx + 1, curr)
            pick = 0
            newStr = curr + arr[idx]
            if isValid(newStr):
                pick = dfs(idx + 1, newStr)

            return max(pick, notPick)

        return dfs(0, "")
