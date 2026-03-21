class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        m = Counter(nums)
        for key,val in m.items():
            heapq.heappush(maxheap,[-val,key])
        ans = []
        while maxheap and k > 0:
            val,key = heapq.heappop(maxheap)
            ans.append(key)
            k-=1
        return ans