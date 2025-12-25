class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        mid = n//2
        ans = [0] * n
        idx1 = 0
        idx2 = 1
        for i in range(0,mid):
            ans[idx1] = nums[i]
            idx1+=2
        for i in range(mid,n):
            ans[idx2] = nums[i]
            idx2+=2
        return ans