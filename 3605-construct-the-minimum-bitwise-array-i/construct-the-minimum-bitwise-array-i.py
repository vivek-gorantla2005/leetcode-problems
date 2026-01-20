class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(1000):
                if (j | j+1) == nums[i] :
                    ans[i] = j
                    break
        
        return ans

        