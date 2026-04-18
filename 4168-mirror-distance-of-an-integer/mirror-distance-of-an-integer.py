class Solution:
    def mirrorDistance(self, n: int) -> int:
        n2 = str(n)[::-1]
        return abs(n - int(n2))