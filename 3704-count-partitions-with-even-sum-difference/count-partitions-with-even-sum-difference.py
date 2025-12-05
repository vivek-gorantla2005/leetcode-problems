class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        S = sum(nums)
        n = len(nums)

        if S % 2 != 0:
            return 0

        return n - 1
