from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        m1 = Counter(words[0])

        for i in range(1, len(words)):
            m2 = Counter(words[i])
            m1 = m1 & m2   

        ans = []
        for ch, count in m1.items():
            ans.extend([ch] * count)

        return ans
