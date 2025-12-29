class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        m = Counter()
        st = 0
        end = 0
        l = 0
        r = 0
        mini = float('inf')

        def valid():
            for ch in c:
                if m[ch] < c[ch]:
                    return False
            return True

        while r < len(s):
            m[s[r]] += 1
            while valid() and l <= r:
                if r - l + 1 < mini:
                    mini = r - l + 1
                    st = l
                    end = r

                m[s[l]] -= 1
                l += 1

            r += 1

        return "" if mini == float('inf') else s[st:end + 1]
