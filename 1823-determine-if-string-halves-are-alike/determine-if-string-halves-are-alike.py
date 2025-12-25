class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = "aeiou"
        h1 = ""
        h2 = ""
        mid = len(s)//2
        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            if i < mid:
                if s[i] in vowels:
                    cnt1+=1
                h1+=s[i]
            else:
                if s[i] in vowels:
                    cnt2+=1
                h2+=s[i]
        
        
        return True if cnt1 == cnt2 else False
            
        