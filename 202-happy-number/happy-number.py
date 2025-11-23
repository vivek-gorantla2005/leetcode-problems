class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n != 1:
            if n in s:        
                return False
            s.add(n)

            sq = 0
            temp = n
            while temp > 0:
                rem = temp % 10
                sq += rem ** 2
                temp //= 10

            n = sq              

        return True
