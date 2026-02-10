class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(len(nums)):
            s1 = set()
            s2 = set()
            for j in range(i,len(nums)):
                if nums[j] % 2 == 0 :
                    s1.add(nums[j])
                else:
                    s2.add(nums[j])
            
                if len(s1) == len(s2):
                    maxi = max(maxi,j-i+1)
            
        return maxi
            
            
        