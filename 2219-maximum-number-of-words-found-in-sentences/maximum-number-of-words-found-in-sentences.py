class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            s = i.split(" ")
            maxi = max(maxi,len(s))
        
        return maxi
        

        