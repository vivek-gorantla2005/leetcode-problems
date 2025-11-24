class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        t="*+/-"
        for c in tokens:
            if c in t:
                op1 = s[-1]
                s.pop()
                op2 = s[-1]
                s.pop()
                if c == '+':
                    s.append(op2+op1)
                elif c=='-':
                    s.append(op2-op1)
                elif c=='*':
                    s.append(op2*op1)
                else:
                    s.append(int(op2/op1))
            else:
                s.append(int(c))
        
        return s[-1]

                
        