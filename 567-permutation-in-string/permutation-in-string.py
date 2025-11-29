class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            s = s2[i:i+len(s1)]
            c2 = Counter(s)
            if c == c2:
                return True
        return False

        