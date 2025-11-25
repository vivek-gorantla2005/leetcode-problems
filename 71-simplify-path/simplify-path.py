class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        curr = ""
        for c in path:
            if c == "/":
                if curr == "..":
                    if s:
                        s.pop()
                elif curr != "" and curr != ".":
                    s.append(curr)
                curr = ""
            else:
                curr += c
        
        # Handle final segment
        if curr == "..":
            if s:
                s.pop()
        elif curr != "" and curr != ".":
            s.append(curr)

        return "/" + "/".join(s)