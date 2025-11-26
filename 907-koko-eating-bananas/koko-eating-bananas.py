class Solution:
    def eat(self, piles, mid, h):
        cnt = 0
        for i in piles:
            cnt += math.ceil(i/mid)
        return cnt <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1                
        high = max(piles)
        mini = float('inf')

        while low <= high:
            mid = (low + high) // 2    

            if self.eat(piles, mid, h):
                mini = min(mini, mid)  
                high = mid - 1
            else:
                low = mid + 1

        return mini
