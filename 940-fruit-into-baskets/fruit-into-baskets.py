class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans =0
        st = 0
        end = 0
        maxi = float("-inf")
        m = Counter()
        n= len(fruits)
        while end < n:
            m[fruits[end]]+=1
            while st < n and len(m) > 2:
                m[fruits[st]]-=1
                if m[fruits[st]] == 0:
                    del m[fruits[st]]
                st+=1
            maxi = max(maxi,end-st+1)
            end+=1
        return maxi
            

        