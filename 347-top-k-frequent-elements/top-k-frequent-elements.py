class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        m = Counter(nums)
        t = m.most_common(k)
        for i in t:
            ans.append(i[0])
        return ans