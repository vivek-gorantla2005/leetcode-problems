class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [[ math.sqrt((i[0] * i[0] ) + (i[1] * i[1])) ,[i[0],i[1]]] for i in points]
        heapq.heapify(minheap)
        
        ans = []
        while k:
            dist,vals = heapq.heappop(minheap)
            ans.append(vals)
            k-=1
        
        return ans

        