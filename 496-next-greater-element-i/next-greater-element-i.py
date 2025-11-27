class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = [0] * len(nums2)
        m = {}

        for i in range(len(nums2)):
            m[nums2[i]] = i
        
        s = []
        
        for i in range(len(nums2) - 1, -1, -1):
            while s and nums2[s[-1]] <= nums2[i]:
                s.pop()
            
            if s:  
                nge[i] = nums2[s[-1]]
            else:
                nge[i] = -1
            
            s.append(i)
        
        ans = []
        for x in nums1:
            ans.append(nge[m[x]])
        
        return ans
