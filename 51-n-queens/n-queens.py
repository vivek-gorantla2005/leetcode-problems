class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for _ in range(n)] 

        def isSafe(r, c):
            # check column
            for i in range(r):
                if board[i][c] == "Q":
                    return False

            # check left diagonal
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # check right diagonal
            i, j = r - 1, c + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def dfs(row):
            if row == n:
                ans.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."

        dfs(0)
        return ans
