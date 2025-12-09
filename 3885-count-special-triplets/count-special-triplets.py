class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        leftFreq = {}
        rightFreq = {}

        # Prepare right frequency counts
        for x in nums:
            rightFreq[x] = rightFreq.get(x, 0) + 1

        ans = 0

        for j in range(n):
            numj = nums[j]

            # nums[j] is no longer in the "right side" after choosing j
            rightFreq[numj] -= 1

            left_needed = 2 * numj
            right_needed = 2 * numj

            leftCount = leftFreq.get(left_needed, 0)
            rightCount = rightFreq.get(right_needed, 0)

            ans = (ans + leftCount * rightCount) % MOD

            # Add nums[j] to left frequency for future
            leftFreq[numj] = leftFreq.get(numj, 0) + 1

        return ans % MOD
        