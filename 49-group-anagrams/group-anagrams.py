class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            
            if key not in m:
                m[key] = []
            
            m[key].append(i)

        ans = []
        for key, vals in m.items():
            ans.append([strs[x] for x in vals])

        return ans
