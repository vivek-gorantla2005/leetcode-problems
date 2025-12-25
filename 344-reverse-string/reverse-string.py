class Solution:
    def reverseString(self, s: List[str]) -> None:
        idx = 0
        n = len(s)
        while(idx < len(s)//2):
            temp = s[idx]
            s[idx]= s[n - idx - 1]
            s[n-idx-1] = temp
            idx+=1
        
        