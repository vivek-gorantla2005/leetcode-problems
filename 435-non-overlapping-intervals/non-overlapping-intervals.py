class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]
        remove = 0
        for i in range(1,len(intervals)):
            currSt = intervals[i][0]
            if prevEnd > currSt:
                remove+=1
                prevEnd = min(prevEnd,intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        
        return remove
        