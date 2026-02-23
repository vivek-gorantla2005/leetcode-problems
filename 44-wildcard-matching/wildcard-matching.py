class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j):
            # both exhausted
            if i < 0 and j < 0:
                return True
            
            # pattern exhausted but string remains
            if j < 0 and i >= 0:
                return False
            
            # string exhausted but pattern remains
            if i < 0 and j >= 0:
                for k in range(j + 1):
                    if p[k] != '*':
                        return False
                return True
            
            if p[j] == s[i] or p[j] == '?':
                return dfs(i - 1, j - 1)
            
            if p[j] == '*':
                return dfs(i - 1, j) or dfs(i, j - 1)
            
            return False
        
        return dfs(len(s) - 1, len(p) - 1)