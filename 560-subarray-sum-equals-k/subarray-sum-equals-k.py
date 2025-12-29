class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        m = {0:1}
        currSum = 0
        for i in range(len(nums)):
            currSum+=nums[i]
            diff = currSum - k
            if diff in m:
                res+=m[diff]
            
            if currSum in m:
                m[currSum] += 1
            else:
                m[currSum] = 1
        
        return res