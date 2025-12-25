class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                ans+=1
        return ans