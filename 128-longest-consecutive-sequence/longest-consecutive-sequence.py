class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)
        maxi = float('-inf')

        for i in s:
            if i - 1 not in s:
                curr = 1
                x = i + 1
                while x in s:
                    curr += 1
                    x += 1
                maxi = max(maxi, curr)
        
        return maxi
