class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * (n + 1)  

        def dfs(i):
            if i == n:
                return True

            if dp[i] != -1:
                return dp[i] == 1

            for word in wordDict:
                currsize = len(word)

                # check bounds
                if i + currsize > n:
                    continue

                # correct substring check
                if s[i : i + currsize] == word and dfs(i + currsize):
                    dp[i] = 1
                    return True

            dp[i] = 0
            return False

        return dfs(0)
