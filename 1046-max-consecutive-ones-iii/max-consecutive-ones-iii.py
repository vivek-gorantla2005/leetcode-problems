class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        r= 0
        maxi = float('-inf')
        zeros = 0
        while r < len(nums):
            if nums[r] == 0:
                zeros+=1
            while zeros > k and l < len(nums):
                if nums[l] == 0:
                    zeros-=1
                l+=1
            maxi = max(maxi,r-l+1)
            r+=1
        return maxi
