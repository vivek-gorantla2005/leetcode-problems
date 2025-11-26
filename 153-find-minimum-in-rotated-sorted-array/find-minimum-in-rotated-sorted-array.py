class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                mini = min (mini,nums[low])
                low = mid + 1
            else:
                mini = min (mini,nums[mid])
                high = mid-1
        return mini
            

        