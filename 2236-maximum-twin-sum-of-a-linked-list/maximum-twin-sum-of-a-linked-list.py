class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        m = {}
        idx = 0
        temp = head
        while temp:
            m[idx] = temp.val
            temp = temp.next
            idx+=1
        
        maxi = float('-inf')
        for i in range(idx//2):
            maxi = max(maxi,(m[i]+m[idx-i-1]))

        return maxi
        