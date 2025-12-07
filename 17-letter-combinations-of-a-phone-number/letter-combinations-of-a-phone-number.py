class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        m = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans = []

        def dfs(idx, curr):
            if idx == len(digits):
                ans.append(curr)
                return

            for c in m[digits[idx]]:
                dfs(idx + 1, curr + c)

        dfs(0, "")
        return ans
