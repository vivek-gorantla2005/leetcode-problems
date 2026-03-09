class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            st = i + 1
            end = n - 1

            while st < end:

                total = nums[i] + nums[st] + nums[end]

                if total > 0:
                    end -= 1

                elif total < 0:
                    st += 1

                else:
                    ans.append([nums[i], nums[st], nums[end]])

                    while st < end and nums[st] == nums[st+1]:
                        st += 1

                    while st < end and nums[end] == nums[end-1]:
                        end -= 1

                    st += 1
                    end -= 1

        return ans