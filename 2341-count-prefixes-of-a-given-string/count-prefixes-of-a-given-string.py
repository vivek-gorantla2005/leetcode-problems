class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for i in words:
            n = len(i)
            if s[:n] == i:
                ans+=1
        return ans
        