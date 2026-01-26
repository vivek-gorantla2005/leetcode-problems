class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mini = float('inf')
        for i in range(1,len(arr)):
            mini = min(mini,abs(arr[i]-arr[i-1]))

        ans = []
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == mini:
                ans.append([arr[i-1],arr[i]])
        
        return ans
        