class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        m = Counter(nums)
        c = m.most_common(k)
        for i in range(len(c)):
            ans.append(c[i][0])
        return ans
        