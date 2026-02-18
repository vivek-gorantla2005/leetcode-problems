class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        ans = 0
        for i in range(len(words)):
            if words[i][:n] == pref:
                ans+=1
        
        return ans

        