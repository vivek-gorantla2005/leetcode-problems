class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = defaultdict(int)
        for i in s:
            c[i]+=1
        
        if len(c) == 1:
            return len(s)

        flag = False
        ans = 0
        for key,val in c.items():
            if val % 2 == 0:
                ans+=val
            else:
                ans+=val-1
                flag= True
        
        if flag:
            ans+=1
            
        return ans
        