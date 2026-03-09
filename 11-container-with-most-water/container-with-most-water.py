class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        st = 0
        end = n-1
        maxi = float('-inf')
        while st < end:
            area = min(height[st],height[end]) * (end-st)
            maxi = max(maxi,area)
            if height[st] < height[end]:
                st+=1
            else:
                end-=1
        return maxi

        