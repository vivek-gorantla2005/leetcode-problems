class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for x in nums:
            heapq.heappush(heap,-x)
        
        while heap and k > 1:
            heapq.heappop(heap)
            k-=1
        
        return -heap[0]