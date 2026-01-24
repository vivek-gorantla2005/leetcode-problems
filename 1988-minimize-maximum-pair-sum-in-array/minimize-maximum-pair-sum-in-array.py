class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        st = 0
        end = len(nums)-1
        maxi = 0
        while st < end:
            maxi = max(maxi,nums[st]+nums[end])
            st+=1
            end-=1
        
        return maxi
