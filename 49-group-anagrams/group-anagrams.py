class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for i in strs:
            curr = "".join(sorted(i))
            m[curr].append(i)

        ans = m.values()
        final = []
        for i in ans:
            final.append(i)
        return final