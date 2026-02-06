class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = {}
        def helper(i,j):
            if i == len(triangle)-1:
                return triangle[i][j]
            if (i,j) in dp:
                return dp[(i,j)]
            d1 = triangle[i][j] + helper(i+1,j)
            d2 = triangle[i][j] + helper(i+1,j+1)

            dp[(i,j)] =  min(d1,d2)
            return dp[(i,j)]
        
        return helper(0,0)


        