class Solution:
    def isPal(self, s: str) -> bool:
        st, end = 0, len(s) - 1
        while st <= end:
            if s[st] != s[end]:
                return False
            st += 1
            end -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans: List[List[str]] = []

        def dfs(curr: List[str], idx: int):
            if idx == len(s):
                ans.append(curr[:])
                return

            for i in range(idx, len(s)):
                substring = s[idx:i+1]       
                if self.isPal(substring):
                    curr.append(substring) 
                    dfs(curr, i+1)           
                    curr.pop()                

        dfs([], 0)
        return ans
