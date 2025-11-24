class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s = ""
        ans = []
        for i in range(len(nums)):
            s+=str(nums[i])
            n = int(s,2)
            if n % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
        