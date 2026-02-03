class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        i = 1

        # strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1:  
            return False

        # strictly decreasing
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        if i == n or nums[i - 1] >= nums[i - 2]:
            return False

        # strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1

        return i == n