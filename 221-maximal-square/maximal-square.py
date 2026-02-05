class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        def helper(i,j):
            if  i >= len(matrix) or j >= len(matrix[0]):
                return 0
            if (i,j) not in dp:
                down = helper(i+1,j)
                right = helper(i,j+1)
                diag = helper(i+1,j+1)
                dp[(i,j)] = 0
                if matrix[i][j] == "1":
                    dp[(i,j)] = 1 + min(right,down,diag)
            
            return dp[(i,j)]
        
        helper(0,0)
        return max(dp.values()) ** 2
            