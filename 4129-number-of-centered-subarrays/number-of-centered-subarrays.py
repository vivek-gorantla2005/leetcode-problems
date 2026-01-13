class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            s = set()
            su = 0
            for j in range(i,len(nums)):
                s.add(nums[j])
                su+=nums[j]
                if su in s:
                    cnt+=1
        return cnt