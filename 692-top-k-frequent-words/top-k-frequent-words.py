class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        m = Counter()
        for w in words:
            m[w]+=1
        
        minheap = []

        for key,val in m.items():
            heapq.heappush(minheap,(-val,key))
        
        return [heapq.heappop(minheap)[1] for _ in range(k)]