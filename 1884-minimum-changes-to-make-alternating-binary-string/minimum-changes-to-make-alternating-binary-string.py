class Solution:
    def minOperations(self, s: str) -> int:
        pattern1 = 0  
        pattern2 = 0 

        for i in range(len(s)):
            # pattern 010101...
            if s[i] != ('0' if i % 2 == 0 else '1'):
                pattern1 += 1

            # pattern 101010...
            if s[i] != ('1' if i % 2 == 0 else '0'):
                pattern2 += 1

        return min(pattern1, pattern2)