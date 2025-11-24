class Solution:
    def isPalindrome(self, s: str) -> bool:
        g = [i for i in s if i.isalnum()]
        g = "".join(g).lower()
        st = 0
        end = len(g)-1
        while st < end:
            if g[st] != g[end]:
                return False
            else:
                st+=1
                end-=1
        return True