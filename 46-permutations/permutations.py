class Solution:
    def permute(self, nums):
        ans = []

        def getpermute(nums, index):
            if index == len(nums):
                ans.append(nums[:]) 
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index] 
                getpermute(nums, index + 1)
                nums[index], nums[i] = nums[i], nums[index] 

        getpermute(nums, 0)
        return ans
