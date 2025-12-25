class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans+="G"
            if i + 1 < len(command) and command[i] == "(" and command[i+1] == ")":
                ans+="o"
            if i + 3 < len(command) and command[i] == "(" and command[i+1] =="a" and command[i+2] == "l" and  command[i+3] == ")":
                ans+="a"
                ans+="l"
        print(ans)
        return ans


        