class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = float('-inf')
        st = 0
        end = len(height)-1
        while st < end:
            area = min(height[st],height[end])*(end-st)
            maxi = max(maxi,area)
            if height[end] <= height[st]:
                end-=1
            else:
                st+=1
        return maxi

        