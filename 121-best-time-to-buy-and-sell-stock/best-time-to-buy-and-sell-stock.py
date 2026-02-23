class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            cost = prices[i] - mini
            total = max(total,cost)
            mini = min(mini,prices[i])
        
        return total