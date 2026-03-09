class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        closestDiff = float('inf')
        ans = 0

        for i in range(n):

            st = i + 1
            end = n - 1

            while st < end:

                curr = nums[i] + nums[st] + nums[end]

                diff = abs(curr - target)

                if diff < closestDiff:
                    closestDiff = diff
                    ans = curr

                if curr < target:
                    st += 1
                else:
                    end -= 1

        return ans