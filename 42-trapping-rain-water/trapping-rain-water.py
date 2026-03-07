class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        rightMax = [0] * n
        leftMax = [0] * n

        rightMax[n-1] = height[n-1]
        leftMax[0] = height[0]


        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        
        for i in range(n):
            leftMax[i] = max(leftMax[i-1],height[i])

        ans = 0
        for i in range(n):
            ans+=min(leftMax[i],rightMax[i]) - height[i]
        
        return ans
                
