class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        se = set(c.values())
        return True if len(se) == 1 else False

        