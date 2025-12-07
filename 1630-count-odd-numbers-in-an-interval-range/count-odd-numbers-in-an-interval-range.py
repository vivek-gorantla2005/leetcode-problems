class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # range odd count = count(high+1) - count(low)
        high_cnt = (high+1)//2
        low_cnt = (low)//2
        return high_cnt - low_cnt