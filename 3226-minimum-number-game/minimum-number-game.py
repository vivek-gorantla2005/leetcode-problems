class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        mini = nums
        heapq.heapify(mini)
        ans = []
        while len(mini) > 1:
            ele1 = heapq.heappop(mini)
            ele2 = heapq.heappop(mini)
            ans.append(ele2)
            ans.append(ele1)
        return ans


        