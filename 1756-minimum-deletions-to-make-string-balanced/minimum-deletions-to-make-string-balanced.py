class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)

        a_right = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            a_right[i] = a_right[i + 1] + (1 if s[i] == 'a' else 0)
        
        res = float('inf')
        b_left = 0
        
        for i in range(n + 1):
            res = min(res, b_left + a_right[i])
            
            if i < n and s[i] == 'b':
                b_left += 1
        
        return res
