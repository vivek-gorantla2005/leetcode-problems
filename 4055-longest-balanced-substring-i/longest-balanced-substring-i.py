class Solution:
    def longestBalanced(self, s: str) -> int:
        maxi = float('-inf')
        for i in range(len(s)):
            m = {}
            for j in range(i,len(s)):
                if s[j] not in m:
                    m[s[j]]=0
                m[s[j]]+=1
                
                se = set(m.values())
                if len(se) == 1:
                    maxi = max(maxi,j-i+1)
        
        return maxi
        