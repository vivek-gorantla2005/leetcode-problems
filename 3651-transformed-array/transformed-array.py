class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                idx = (i + nums[i]) % n
                res[i] = nums[idx]
            elif nums[i] < 0:
                idx = (i + nums[i])%n
                res[i] = nums[idx]
            else:
                res[i] = nums[i]
        
        return res