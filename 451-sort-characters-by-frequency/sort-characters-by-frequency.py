from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        m = Counter(s)              
        chars = list(s)             
        chars.sort(key=lambda x: (-m[x],x))
        return "".join(chars)      
