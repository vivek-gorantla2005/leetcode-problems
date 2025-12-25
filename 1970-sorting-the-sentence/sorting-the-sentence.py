class Solution:
    def sortSentence(self, s: str) -> str:
        s2 = s.split(" ")
        s3 = sorted(s2,key=lambda x : x[len(x)-1])
        ans = []
        for x in s3:
            ans.append(x[:-1])
        return " ".join(ans)
        