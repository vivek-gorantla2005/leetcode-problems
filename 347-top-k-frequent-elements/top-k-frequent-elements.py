class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        heap = []
        for key,val in m.items():
            heapq.heappush(heap,(-val,key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans

        