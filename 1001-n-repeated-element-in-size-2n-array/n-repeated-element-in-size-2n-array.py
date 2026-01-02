class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m = Counter(nums)
        n = len(nums)/2
        for key,val in m.items():
            if val>=n:
                return key
        return -1

