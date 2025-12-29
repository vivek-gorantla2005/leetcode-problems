class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = Counter(s1)
        m2 = Counter()
        l = 0
        r = 0
        k = len(s1)

        while r < len(s2):
            m2[s2[r]] += 1

            while r - l + 1 > k:
                m2[s2[l]] -= 1
                if m2[s2[l]] == 0:
                    del m2[s2[l]]
                l += 1

            if m1 == m2:
                return True

            r += 1

        return False
