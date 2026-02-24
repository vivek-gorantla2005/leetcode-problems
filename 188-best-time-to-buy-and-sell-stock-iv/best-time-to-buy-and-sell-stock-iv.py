class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        curr = [[0] * (k+1) for _ in range(2)] 
        nxt = [[0] * (k+1) for _ in range(2)] 

        for idx in range(n-1,-1,-1):
            for buy in range(0,2):
                for cap in range(1,k+1):
                    if buy:
                        profit = max(
                            -prices[idx] + nxt[0][cap],   
                            nxt[1][cap]
                        )
                    else:
                        profit = max(
                            prices[idx] + nxt[1][cap-1], 
                            nxt[0][cap]               
                        )

                    curr[buy][cap] = profit

            nxt = curr

        return nxt[1][k]

        