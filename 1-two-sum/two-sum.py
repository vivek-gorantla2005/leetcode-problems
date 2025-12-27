class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = i

        for i in range(len(nums)):
            newTar = target - nums[i]
            if newTar in m and m[newTar] != i:
                return [i, m[newTar]]

        return []
