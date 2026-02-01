class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ele1 = float('inf')
        ele2 = float('inf')
        for i in nums:
            if i <= ele1:
                ele1 = i
            elif i <= ele2 and i > ele1 :
                ele2 = i
            else:
                return True
        
        return False
        


            