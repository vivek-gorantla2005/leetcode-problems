class Solution:
    def isPossible(self, batteries, n, curr):
        s = 0
        less = 0

        for i in batteries:
            if i < curr:
                s += i
            else:
                s+=curr
        
        return (s >= curr * n)

        

    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        maxi = float('-inf')
        low = 0
        high = sum(batteries)

        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(batteries, n, mid):
                maxi = max(maxi, mid)
                low = mid + 1
            else:
                high = mid - 1

        return maxi
