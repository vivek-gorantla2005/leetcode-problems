class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = []
        ans.append(points[0])
        for i in range(len(points)):
            if ans[-1][1] >= points[i][0]:
                ans[-1][1] = min(ans[-1][1],points[i][1])
            else:
                ans.append(points[i])
        
        return len(ans)
        