class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = Counter(nums)               
        ans = []
        mc = t.most_common(k)
        for i in range(k):
            ans.append(mc[i][0])
        return ans
