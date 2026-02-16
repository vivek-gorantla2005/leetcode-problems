class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i in nums:
            #pop bigger previous elements
            while stack and stack[-1] > i:
                stack.pop()
                        
            if i > 0 and (not stack or i > stack[-1]):
                res+=1
                stack.append(i)

        return res
        