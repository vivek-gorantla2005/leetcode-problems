from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        m = Counter()
        l = 0
        r = 0
        curr = 0     
        minLen = float('inf')
        st = 0
        end = 0

        while r < len(s):
            curr += 1
            if s[r] in c:
                m[s[r]] += 1

            # check validity: all characters of t must have required counts
            def valid():
                for ch in c:
                    if m[ch] < c[ch]:
                        return False
                return True

            if valid() and curr < minLen:
                minLen = curr
                st = l
                end = r

            # shrink window from left
            while valid() and l < len(s):
                if s[l] in c:
                    m[s[l]] -= 1
                l += 1
                curr -= 1   

                if valid() and curr < minLen:
                    minLen = curr
                    st = l
                    end = r

            r += 1

        if minLen == float('inf'):
            return ""
        return s[st:end+1]
