class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n):

                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                st = j + 1
                end = n - 1

                while st < end:

                    s = nums[i] + nums[j] + nums[st] + nums[end]

                    if s > target:
                        end -= 1

                    elif s < target:
                        st += 1

                    else:
                        ans.append([nums[i], nums[j], nums[st], nums[end]])

                        st += 1
                        end -= 1

                        while st < end and nums[st] == nums[st-1]:
                            st += 1

                        while st < end and nums[end] == nums[end+1]:
                            end -= 1

        return ans