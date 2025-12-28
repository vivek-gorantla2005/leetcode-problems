class Solution:
    def maximumCount(self, grid: List[int]) -> int:
        pos = 0
        neg = 0
        for i in range(len(grid)):
            if grid[i] > 0:
                pos+=1
            if grid[i] < 0:
                neg+=1
        return max(pos,neg)