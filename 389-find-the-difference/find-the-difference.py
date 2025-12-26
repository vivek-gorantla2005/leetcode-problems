class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = Counter(s)
        s2 = Counter(t)
        for key,val in s2.items():
            if key not in c or val > c[key]:
                return key