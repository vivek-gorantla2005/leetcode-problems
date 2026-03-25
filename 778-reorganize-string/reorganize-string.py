class Solution:
    def reorganizeString(self, s: str) -> str:
        m = Counter(s)
        maxheap = [[-cnt, char] for char, cnt in m.items()]
        heapq.heapify(maxheap)

        prev = None
        ans = ""

        while maxheap:
            cnt, char = heapq.heappop(maxheap)
            ans += char
            cnt += 1 
                        
            if prev:
                heapq.heappush(maxheap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]


        return ans if len(ans) == len(s) else ""