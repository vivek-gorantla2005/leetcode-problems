class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        open = "([{"
        close = ")]}"
        if s[0] in close:
            return False
        for i in s:
            if i in open:
                st.append(i)
            if not st and i in close :
                return False
            if i in close and st:
                if i == ')' and st[-1] == '(':
                    st.pop()
                elif i == ']' and st[-1] == '[':
                    st.pop()
                elif i == '}' and st[-1] == '{':
                    st.pop()
                else:
                    return False
        
        return True if len(st) == 0 else False