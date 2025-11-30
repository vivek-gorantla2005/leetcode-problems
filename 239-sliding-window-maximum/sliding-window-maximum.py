from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        q = deque() 
        ans = []

        for r in range(len(nums)):
            if q and q[0] < r - k + 1:
                q.popleft()

            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if r >= k - 1:
                ans.append(nums[q[0]])

        return ans
