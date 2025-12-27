class Solution:
    def customSortString(self, order: str, s: str) -> str:
        m = {}
        for i in range(len(order)):
            m[i] = order[i]

        ans = ""

        for key, val in m.items():
            while val in s:
                ans += val
                s = s.replace(val, "", 1)

        ans += s

        return ans
