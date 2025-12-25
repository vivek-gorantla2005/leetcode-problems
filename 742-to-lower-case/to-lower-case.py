class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ""
        for i in s:
            if i.upper():
                ans+=i.lower()
            else:
                ans+=i
        return ans
        