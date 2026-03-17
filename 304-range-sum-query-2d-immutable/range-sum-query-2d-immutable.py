class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])

        self.prefix = [[0]*m for _ in range(n)]

        self.prefix[0][0] = matrix[0][0]

        # first row
        for j in range(1, m):
            self.prefix[0][j] = self.prefix[0][j-1] + matrix[0][j]

        # first column
        for i in range(1, n):
            self.prefix[i][0] = self.prefix[i-1][0] + matrix[i][0]

        # fill rest
        for i in range(1, n):
            for j in range(1, m):
                self.prefix[i][j] = (
                    matrix[i][j]
                    + self.prefix[i-1][j]
                    + self.prefix[i][j-1]
                    - self.prefix[i-1][j-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.prefix[row2][col2]

        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        top_left = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return total - top - left + top_left