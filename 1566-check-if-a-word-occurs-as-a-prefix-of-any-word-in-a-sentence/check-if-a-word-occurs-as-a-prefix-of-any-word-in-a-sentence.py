class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s = sentence.split(" ")
        for i in range(len(s)):
            n = len(s[i])
            m = len(searchWord)
            if s[i][:m] == searchWord:
                return i+1
        
        return -1

        