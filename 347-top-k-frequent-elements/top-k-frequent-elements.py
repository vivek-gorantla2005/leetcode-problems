class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        m = Counter(nums)
        for key,val in m.items():
            maxheap.append([-val,key])
        heapq.heapify(maxheap)
        ans = []
        while maxheap and k > 0:
            val,key = heapq.heappop(maxheap)
            ans.append(key)
            k-=1
        return ans