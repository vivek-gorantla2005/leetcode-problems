class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod1 = 1
        prod2 = 1
        pre = []
        suff = []

        # prefix product
        for i in nums:
            prod1 *= i
            pre.append(prod1)

        # suffix product
        for i in range(len(nums) - 1, -1, -1):  
            prod2 *= nums[i]
            suff.append(prod2)

        # reverse suffix to match indices
        suff = suff[::-1]

        ans = []
        n = len(nums)

        for i in range(n):
            if 0 < i < n - 1:     # middle
                ans.append(pre[i - 1] * suff[i + 1])
            elif i == n - 1:      # last element
                ans.append(pre[i - 1])
            else:                 # first element (i == 0)
                ans.append(suff[i + 1])

        return ans
