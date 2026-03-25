class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = defaultdict(list)
        for i in range(len(s)):
            m[s[i]].append(i)
    
        intervals = [[val[0],val[len(val)-1]] for key,val in m.items()]
        intervals.sort()

        ans = []
        ans.append(intervals[0])
        for i in range(1,len(intervals)):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])

        return [a[1] - a[0] + 1 for a in ans]



