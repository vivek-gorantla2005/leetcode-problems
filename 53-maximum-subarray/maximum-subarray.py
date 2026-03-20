class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        maxi = float('-inf')
        for i in nums:
            prefix+=i
            maxi = max(maxi,prefix)
            if prefix < 0:
                prefix = 0
        
        return maxi
        