class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        val = 1
        while val * 2 < n:
            val = val * 2
        
        return  1 + min(self.minOperations(val*2-n),self.minOperations(n-val))

        