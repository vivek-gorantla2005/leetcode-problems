class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        resSize=  n * 2
        ans = [0]*resSize
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans