class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = []
        for key,val in c1.items():
            if key in c2.keys():
                r = min(val,c2[key])
                for i in range(r):
                    ans.append(key)
        return ans