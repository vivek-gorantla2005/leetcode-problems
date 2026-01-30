class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        c = Counter()
        for i in range(len(senders)):
            words = messages[i].split(" ")
            c[senders[i]]+=len(words)
        
        maxi = max(c.values())

        l = float("-inf")
        s = ""
        for key,val in c.items():
            if val == maxi:
                if key > s:
                    l = len(key)
                    s = key

        return s
        
        