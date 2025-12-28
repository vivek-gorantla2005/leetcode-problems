class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range (len(nums)):
            for j in range(len(nums)):
                if i < j and abs(nums[i] - nums[j]) == k:
                    ans+=1
        return ans