class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        ans = []
        for i in range(len(s)):
            if s[i] == '(':
                st.append(['(',i])
            if s[i] == ')':
                if st:
                    p,idx = st.pop()
                    ans.append([idx,i])
        
        final = [""] * len(s)
        for openidx,closeidx in ans:
            final[openidx] = "("
            final[closeidx] = ")"
        
        for i in range(len(s)):
            if s[i] not in "()":
                final[i] = s[i]
        
        return "".join(final)
        


            