class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n+1):
            b = bin(i)
            b = b[2:]
            cnt = 0
            for j in b:
                if j == "1":
                    cnt+=1
            
            ans.append(cnt)
        
        return ans