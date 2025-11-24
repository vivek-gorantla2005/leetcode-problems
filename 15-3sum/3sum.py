class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = set()
        nums.sort()
        for i in range(len(nums)):
            tar = -nums[i]
            j = i+1
            end = len(nums)-1
            while j < end:
                if nums[j] + nums[end] == tar:
                    sol.add((nums[i],nums[j],nums[end]))
                    j += 1
                    end -= 1
                elif nums[j] + nums[end] < tar:
                    j+=1
                else:
                    end-=1
        return [list(t) for t in sol]


        