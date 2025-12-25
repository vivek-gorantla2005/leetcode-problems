class Solution:
    def isPalindrome(self, s: str) -> bool:
        ms = ""
        for i in s:
            if i.isspace() or not i.isalnum():
                continue
            if 'A' <= i <= 'Z':
                ms+=chr(ord(i) + 32)
            else:
                ms+=i
        r = ms[::-1]
        if ms == r:
            return True
        return False
        
        