class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prereq:
            adj[b].append(a)
            indegree[a] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        completed = 0
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            completed += 1

            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        if len(ans) == numCourses:
            return ans
        else:
            return []