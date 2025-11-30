class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        idx = 1
        while idx < len(nums)-1 and nums[idx-1] != nums[idx]:
            idx+=1
        
        return nums[idx]
        