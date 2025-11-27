class Solution:
    def nse(self, heights):
        n = len(heights)
        nse = [0] * n
        s = []

        for i in range(n - 1, -1, -1):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            
            if s:
                nse[i] = s[-1]
            else:
                nse[i] = n
            s.append(i)
        return nse
    

    def pse(self, heights):
        n = len(heights)
        pse = [0] * n
        s = []

        for i in range(n):
            while s and heights[s[-1]] >= heights[i]:
                s.pop()
            
            if s:
                pse[i] = s[-1]
            else:
                pse[i] = -1
            s.append(i)
        return pse
    

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = self.pse(heights)
        right = self.nse(heights)

        maxarea = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            maxarea = max(maxarea, area)
        return maxarea
    

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        
        prefix = [ [0]*m for _ in range(n) ]

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "0":    
                    prefix[i][j] = 0
                else:
                    if i == 0:
                        prefix[i][j] = 1
                    else:
                        prefix[i][j] = prefix[i-1][j] + 1

        ans = 0
        for i in range(n):
            ans = max(ans, self.largestRectangleArea(prefix[i]))

        return ans
