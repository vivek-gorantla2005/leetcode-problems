class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)
        maxheap = [-cnt for cnt in c.values()]
        heapq.heapify(maxheap)

        q = deque()
        time = 0

        while maxheap or q:
            time+=1
            if maxheap:
                currtask = 1+heapq.heappop(maxheap)
                if currtask:
                    q.append([currtask,time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time

            

        


        