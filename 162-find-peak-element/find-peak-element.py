class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 1] > nums[n - 2]:
            return n - 1

        st = 1
        end = n - 2

        while st <= end:
            mid = (st + end) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            # increasing slope → go right
            elif nums[mid] > nums[mid - 1]:
                st = mid + 1

            # decreasing slope → go left
            else:
                end = mid - 1

        return -1