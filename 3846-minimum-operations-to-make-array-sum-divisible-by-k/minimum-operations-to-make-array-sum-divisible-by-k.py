class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s = sum(nums)
        rem = s % k
        return rem
        