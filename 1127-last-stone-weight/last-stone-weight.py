class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-i for i in stones]
        heapq.heapify(maxHeap)
        
        while maxHeap and len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            if stone1 != stone2:
                heapq.heappush(maxHeap,-abs(stone1-stone2))
        
        return -maxHeap[0] if maxHeap else 0
        

        