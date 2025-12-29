class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = Counter()
        l = 0
        r = 0
        maxi = float('-inf')
        maxf = float('-inf')
        while r < len(s):
            m[s[r]]+=1
            maxf = max(maxf,m[s[r]])
            while r-l+1 - maxf > k and l < len(s):
                m[s[l]]-=1
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1
    
        return maxi
        