class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        for key,val in c1.items():
            if abs(c2[key] - val) > 3:
                return False

        for key,val in c2.items():
            if abs(c1[key] - val) > 3:
                return False

        return True
        