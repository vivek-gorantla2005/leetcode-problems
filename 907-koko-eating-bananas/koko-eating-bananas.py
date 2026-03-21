class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(mid):
            hours = 0
            for b in piles:
                hours +=math.ceil(b/mid)
            
            return hours <= h

        st = 1
        high = max(piles)
        ans = high

        while st <= high:
            mid = (st + high) // 2

            if helper(mid):
                ans = mid
                high = mid - 1
            else:
                st = mid + 1

        return ans